from datetime import datetime


class WaterManager:
    def __init__(self, user_data):
        self.user_data = user_data

    async def record_water_intake(self, update, context):
        chat_id = update.effective_chat.id
        if chat_id not in self.user_data:
            await update.message.reply_text("Primero ejecuta /start.")
            return
        data = self.user_data[chat_id]
        if data["completed"]:
            await update.message.reply_text("🎉 ¡Ya cumpliste tu objetivo de hoy!")
            return
        data["water"] += 1
        if data["water"] >= data["goal"]:
            data["completed"] = True
            await update.message.reply_text(
                f"🎉 ¡Objetivo alcanzado! Bebiste {data['goal']} vasos hoy."
            )
        else:
            await update.message.reply_text(
                f"💧 Vaso registrado. Total hoy: {data['water']}/{data['goal']}"
            )

    async def update_goal(self, update, context):
        chat_id = update.effective_chat.id
        if len(context.args) != 1 or not context.args[0].isdigit():
            await update.message.reply_text("⚠️ Uso correcto: /objetivo 10")
            return
        new_goal = int(context.args[0])
        if chat_id not in self.user_data:
            self.user_data[chat_id] = {
                "water": 0,
                "goal": new_goal,
                "completed": False,
                "work_start": 9,
                "work_end": 17,
            }
        else:
            self.user_data[chat_id]["goal"] = new_goal
            self.user_data[chat_id]["completed"] = (
                self.user_data[chat_id]["water"] >= new_goal
            )
        await update.message.reply_text(
            f"✅ Objetivo actualizado: {new_goal} vasos diarios"
        )

    async def send_hydration_reminders(self, application):
        now = datetime.now()
        if 8 <= now.hour < 24:
            for chat_id, data in self.user_data.items():
                if data["water"] < data["goal"] and not data["completed"]:
                    await application.bot.send_message(
                        chat_id=chat_id,
                        text=(
                            f"💧 ¡Hora de beber agua!\n"
                            f"Vasos hoy: {data['water']}/{data['goal']}"
                        ),
                    )
