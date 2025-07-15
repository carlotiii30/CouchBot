# 🛋️ HealthyCouchBot — Tu compañero saludable en Telegram

**HealthyCouchBot** es un bot de Telegram público que te recuerda moverte y mantenerte hidratada a lo largo del día. Ideal para cualquier persona que trabaje muchas horas sentada y quiera adoptar hábitos más saludables.

---

## 🧠 Funcionalidades

✅ Recordatorios automáticos para beber agua cada 90 minutos  
✅ Objetivo diario configurable (por defecto: 8 vasos = 2 litros)  
✅ Registro manual de agua con el comando `/agua`  
✅ Recordatorios para moverse cada hora durante tu jornada laboral  
✅ Comando `/horario` para definir tu jornada laboral

---

## 🚀 ¿Cómo usar HealthyCouchBot?

1. **Busca el bot en Telegram**:  
   Ve a [https://t.me/HealthyCouchBot](https://t.me/HealthyCouchBot) o búscalo como `@HealthyCouchBot`.

2. **Escribe `/start` para comenzar**  
   El bot guardará tus datos de manera individual para enviarte recordatorios personalizados.

---

## 💬 Comandos disponibles

- `/start` → Inicia el bot y crea tu perfil saludable.
- `/agua` → Registra manualmente un vaso de agua.
- `/objetivo N` → Cambia el objetivo diario a `N` vasos (por defecto: 8).
- `/horario HH-HH` → Define tu horario laboral para los recordatorios de moverse (por defecto: 9-17).

---

## 🕒 Comportamiento diario

- HealthyCouchBot te envía recordatorios **cada 90 minutos** si aún no has llegado a tu objetivo de agua.
- Solo te recuerda hidratarte entre las **08:00 y 23:59**.
- Cuando alcanzas tu meta, **deja de recordarte** ese día.
- A las 00:00, se **reinicia el contador** automáticamente.
- Cada hora durante tu horario laboral, te recuerda **moverte y estirarte un poco**.

---

## 🛠️ Desarrolladores

Si quieres desplegar tu propia versión:

1. **Crea un bot con BotFather** en Telegram y obtén tu token.
2. **Instala las dependencias necesarias**:

```bash
pip install python-telegram-bot apscheduler
```

3. **Cambia el token en `.env`**:

```dotenv
BOT_TOKEN=TU_TOKEN_AQUI
```

4. **Ejecuta el bot**:

```bash
python bot/main.py
```

### 🚀 Despliegue automático con Render

Si tu repositorio tiene `render.yaml` y `requirements.txt`, puedes desplegarlo automáticamente:

1. Sube tu código a GitHub.
2. Entra en [https://render.com](https://render.com) y crea un nuevo Web Service.
3. Conecta tu repositorio y añade la variable `BOT_TOKEN` como variable de entorno.
4. Render instalará todo y ejecutará el bot automáticamente.

---

## 🙋‍♀️ Hecho con ❤️ por Carlota

HealthyCouchBot nació como herramienta personal de bienestar, y ahora está disponible públicamente para cualquiera que quiera mejorar sus hábitos de salud mientras trabaja.

---

## 🛡️ Licencia

MIT — Puedes usar, modificar y compartir **HealthyCouchBot** libremente.