# 🗓️ Discord Planning Bot

A Discord bot that pings a specific role every **Saturday and Sunday at 9PM (Paris time)** with a planning link, and deletes the message exactly **23h59 later**. Built with `discord.py`, scheduled with `APScheduler`.

> Made by **monkey_26** 🐒

---

## 📌 Features

- Sends a ping to a specific role every weekend at 21:00
- Includes a Google Sheet planning link
- Automatically reacts to its own message with ✅
- Deletes the message 23h59 after posting
- Includes a `!test` command to verify the bot is alive

---

## 🚀 Deploy with Render (as Background Worker)

1. Push your code to GitHub
2. Go to [Render.com](https://render.com)
3. Create a **new Web Service**:
   - Type: **Background Worker**
   - Environment: **Python 3**
   - Build Command: `pip install -r src/requirements.txt`
   - Start Command: `python src/main.py`
4. In **Environment > Secret Files** or **Environment Variables**, add:
    - DISCORD_TOKEN=your-bot-token
    - CHANNEL_ID=your-text-channel-id

---

## 📁 Project structure

```bash
.
├── src/
│   ├── main.py             # Bot code
│   ├── .env                # Environment variables (not pushed)
│   └── requirements.txt    # Python dependencies
├── .gitignore              # Prevents pushing sensitive files (like .env)
└── README.md               # Project documentation
```

---

## 🔐 .env file example (in src/.env)

- DISCORD_TOKEN=your_discord_token_here
- CHANNEL_ID=your_text_channel_id

Make sure `.env` is listed in `.gitignore` and **never push it** to GitHub.

---

## 🧪 Local testing

```bash
pip install -r src/requirements.txt
python src/main.py
```

Use `!test` in Discord to see if the bot is running correctly.

---

## 📦 Requirements

Make sure your `src/requirements.txt` contains:
```
discord.py
python-dotenv
APScheduler
```

---

## 🤖 Bot Status

You can see the bot's status message on Discord as:
```
🔔 Planning bot for the weekend
Made by monkey_26 🐒
```

---

## 💬 Questions?

Feel free to open an issue or DM monkey_26 on Discord.

---
