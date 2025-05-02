"""
Discord Planning Bot
---------------------

This bot sends a planning reminder every Saturday and Sunday at 21:00 (Paris time) and deletes the message exactly 23h59 later. It also reacts with a ✅ to help track planning completion.

Author: monkey_26 🐒
Version: 1.0
License: MIT

Dependencies:
- discord.py
- APScheduler
- python-dotenv

Usage:
- Run as a background worker (e.g. on Render)
- Configure via .env file (DISCORD_TOKEN, CHANNEL_ID)
"""

import os
import discord
import asyncio
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv

# Parameters
ROLE_ID_XERO = 1274719485672034475
URL_PLANNING = "https://docs.google.com/spreadsheets/d/10eZ3HxMNKAkCs0WNtHlC5ZaLAmRYVRn88_Hc7dRwb6M/edit?gid=2125886037#gid=2125886037"

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not TOKEN or not CHANNEL_ID:
    raise ValueError("Please set DISCORD_TOKEN and CHANNEL_ID in .env file")

# Set up Discord bot with proper intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Set up scheduler
scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    """
    Schedule the bot message
    """
    print(f"Connecté en tant que {bot.user}")
    try:
        scheduler.add_job(send_ping, CronTrigger(day_of_week='sat,sun', hour=21, minute=0, timezone="Europe/Paris"))
    except Exception as e:
        print(f"Error setting up scheduler: {e}")

async def send_ping():
    """
    Sends a ping message with the planning link to a specific role,
    reacts with a ✅, and deletes the message 23h59 later.
    """
    try:
        channel = bot.get_channel(int(CHANNEL_ID))
        if isinstance(channel, discord.TextChannel):
            message = await channel.send(f"🔔 <@&{ROLE_ID_XERO}>\n Merci de mettre à jour votre planning : {URL_PLANNING}\n ✅ = Planning mis à jour")
            await message.add_reaction("✅")  # Replace ROLE_ID with your actual role ID
            await asyncio.sleep(86340)  # Attendre 23h59 après avoir envoyé le message
            await message.delete()   # Supprimer le message
        else:
            print(f"Channel with ID {CHANNEL_ID} is not a text channel")
    except Exception as e:
        print(f"Error sending ping: {e}")

@bot.command()
async def test(ctx):
    """
    Responds with a confirmation that the bot is active.
    """
    message = await ctx.send("Bot actif ! ✅")
    await asyncio.sleep(10)
    await message.delete()

@bot.command()
async def credits(ctx):
    """
    Responds with credits and deletes the message 1min later.
    """
    message = await ctx.send("Bot crée par Monkey_26 🐒")
    await asyncio.sleep(60)
    await message.delete()

# Start bot
bot.run(TOKEN)