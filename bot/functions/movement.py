from datetime import datetime


class MovementManager:
    def __init__(self, user_data):
        self.user_data = user_data

    async def send_move_reminders(self, application):
        now = datetime.now()
        for chat_id, data in self.user_data.items():
            start = data.get("work_start", 9)
            end = data.get("work_end", 17)
            if start <= now.hour < end:
                await application.bot.send_message(
                    chat_id=chat_id,
                    text="🚶 ¡Hora de moverse! Levántate, estira un poco y da una vuelta.",
                )

    async def set_work_schedule(self, update, context):
        chat_id = update.effective_chat.id
        if len(context.args) != 1 or "-" not in context.args[0]:
            await update.message.reply_text("⚠️ Uso correcto: /horario 09-17")
            return
        try:
            start, end = map(int, context.args[0].split("-"))
            if not (0 <= start < 24 and 0 < end <= 24 and start < end):
                raise ValueError
            if chat_id not in self.user_data:
                self.user_data[chat_id] = {}
            self.user_data[chat_id]["work_start"] = start
            self.user_data[chat_id]["work_end"] = end
            await update.message.reply_text(
                f"🕐 Jornada laboral configurada: {start}:00 a {end}:00"
            )
        except ValueError:
            await update.message.reply_text(
                "❌ Formato incorrecto. Ejemplo válido: /horario 09-17"
            )
