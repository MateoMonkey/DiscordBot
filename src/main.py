"""
Discord Planning Bot
---------------------

This bot sends a planning reminder every Saturday at 20:00 (Paris time) and deletes the message exactly 27 later. It also reacts with a ✅ to help track planning completion.

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
ROLE_ID_XERO = 1378817361800462402 # Replace ROLE_ID with your actual role ID

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
URL_PLANNING = os.getenv("URL_PLANNING")

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
    if not scheduler.get_job("weekly_ping"):
        try:
            scheduler.remove_all_jobs()
            scheduler.add_job(send_ping, CronTrigger(day_of_week='sat', hour=20, minute=0, timezone="Europe/Paris")),id=="weekly_ping"
            scheduler.start()
            await bot.tree.sync()
            print("Commandes slash synchronisées.")
        except Exception as e:
            print(f"Error setting up scheduler: {e}")
    else:
        print("Le job 'weekly_ping' est déjà programmé.")

async def send_ping():
    """
    Sends a ping message with the planning link to a specific role,
    reacts with a ✅, and deletes the message 27h later.
    """
    try:
        channel = bot.get_channel(int(CHANNEL_ID))
        if isinstance(channel, discord.TextChannel):
            message = await channel.send(f"🔔 Bonsoir <@&{ROLE_ID_XERO}>, pensez à remplir vos disponibilités de la semaine prochaine s'il vous plait !\n {URL_PLANNING}\n ✅ = Planning mis à jour")
            await message.add_reaction("✅") 
            await asyncio.sleep(97200)  # Wait 27h before the message is deleted.
            await message.delete()   # Delete the message.
        else:
            print(f"Channel with ID {CHANNEL_ID} is not a text channel")
    except Exception as e:
        print(f"Error sending ping: {e}")

# Command for a test
"""
Responds with a confirmation that the bot is active.
"""
@bot.tree.command(name="test", description="Vérifie si le bot est actif")
async def slash_test(interaction: discord.Interaction):
    await interaction.response.send_message("Bot actif ! ✅", ephemeral=True)

# Command for credits
"""
Responds with credits.
"""
@bot.tree.command(name="credits", description="Affiche les crédits du bot")
async def slash_credits(interaction: discord.Interaction):
    await interaction.response.send_message("Bot créé par Monkey_26 🐒", ephemeral=True)

# Command for planning URL
"""
Responds with URL
"""
@bot.tree.command(name="planning", description="Affiche le lien vers le planning")
async def slash_planning(interaction: discord.Interaction):
    await interaction.response.send_message(f"Voici l'URL : {URL_PLANNING}", ephemeral=True)

# Start bot
bot.run(TOKEN)