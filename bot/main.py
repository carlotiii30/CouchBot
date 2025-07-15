import os
import nest_asyncio
import asyncio
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import ApplicationBuilder, CommandHandler
from functions.water import WaterManager
from functions.movement import MovementManager
from threading import Thread
from flask import Flask

# === Setup ===
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

user_data = {}
water_manager = WaterManager(user_data)
movement_manager = MovementManager(user_data)


# === Telegram Handlers ===
async def start(update, context):
    chat_id = update.effective_chat.id
    user_data[chat_id] = {
        "water": 0,
        "goal": 8,
        "completed": False,
        "work_start": 9,
        "work_end": 17,
    }
    await update.message.reply_text(
        "✅ ¡Hola! Soy CouchBot. Te ayudaré a mantenerte hidratada y activa.\n"
        "💧 Usa /agua para registrar un vaso de agua.\n"
        "🎯 Usa /objetivo N para cambiar tu objetivo de vasos diarios.\n"
        "🕐 Usa /horario HH-HH para definir tu jornada laboral."
    )


def reset_daily_data():
    for data in user_data.values():
        data["water"] = 0
        data["completed"] = False
    print("🔄 Contadores reiniciados.")


# === Flask app para Render ===
flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return "CouchBot está corriendo 🚀"


def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)


# === Telegram bot runner ===
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        CommandHandler(
            "agua",
            lambda update, context: water_manager.record_water_intake(update, context),
        )
    )
    app.add_handler(
        CommandHandler(
            "objetivo",
            lambda update, context: water_manager.update_goal(update, context),
        )
    )
    app.add_handler(
        CommandHandler(
            "horario",
            lambda update, context: movement_manager.set_work_schedule(update, context),
        )
    )

    scheduler = BackgroundScheduler(timezone="Europe/Madrid")
    scheduler.add_job(
        lambda: water_manager.send_hydration_reminders(app), "interval", minutes=90
    )
    scheduler.add_job(
        lambda: movement_manager.send_move_reminders(app), "cron", minute=0
    )
    scheduler.add_job(reset_daily_data, "cron", hour=0, minute=0)
    scheduler.start()

    print("🚀 CouchBot en marcha...")
    await app.run_polling()


if __name__ == "__main__":
    nest_asyncio.apply()

    # Iniciar Flask en hilo paralelo
    Thread(target=run_flask).start()

    # Ejecutar bot de Telegram
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
