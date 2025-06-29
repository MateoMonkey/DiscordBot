# 🗓️ Discord Planning Bot

A Discord bot that pings a specific role every **Saturday at 8PM (Paris time)** with a planning link, and deletes the message exactly **27h later**. Built with `discord.py`, scheduled with `APScheduler`.

> Made by **monkey_26** 🐒

---

## 📌 Features

- Sends a ping to a specific role every saturday at 20:00
- Includes a Google Sheet planning link
- Automatically reacts to its own message with ✅
- Deletes the message 27h after posting
- Includes a `/test` command to verify the bot is alive, `/credits` for credits and `/planning` for the Google doc planning URL.

---

## 🚀 Deploy with Docker

1. Push your code to GitHub
2. Log on your sever (ssh)
3. **Create** a docker image
    - `docker build -t mateomonkey/discord_bot src/`
    - `docker run -d --name discord-bot mateomonkey/discord_bot`
    - `docker push mateomonkey/discord_bot`
4. **Check** the docker image
    - `sudo docker ps -a`
    - `sudo docker image ls`
5. **Stop and delete** the docker image
    - `sudo docker stop discord-bot`
    - `sudo docker rm discord-bot`
    - `docker rmi mateomonkey/discord_bot:latest python:3.12-slim`

---

## 🛡️ CI / Security Scan

A GitHub Actions pipeline is configured to:

- ✅ Automatically scan for vulnerabilities in:
  - The Docker image (`src/Dockerfile`)
- 🕵️ Run every **push**, every **PR**, and **weekly** on Sundays at midnight

You can find this in:  
`.github/workflows/security-scan.yml`

---

## 📁 Project structure

```bash
.
├── src/
│   ├── main.py             # Bot code
│   ├── .env                # Environment variables (not pushed)
│   ├── Dockerfile          # Dockerfile
│   └── requirements.txt    # Python dependencies
├── docker-compose.yml      # Docker compose
├── .gitignore              # Prevents pushing sensitive files (like .env)
├── .github/
│   └── workflows/
│       └── security-scan.yml # GitHub Actions pipeline (build + Trivy scan)
└── README.md               # Project documentation
```

---

## 🔐 .env file example (in src/.env)

```env
DISCORD_TOKEN=your_discord_token_here
CHANNEL_ID=your_text_channel_id
```

Make sure `.env` is listed in `.gitignore` and **never push it** to GitHub.

---

## 🧪 Local testing

```bash
pip install -r src/requirements.txt
python src/main.py
```

Use `/test` in Discord to see if the bot is running correctly.

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
