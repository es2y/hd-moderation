import discord
from discord.ext import commands
from discord import app_commands, ui
import asyncio
import json
from Utils.config import BOT_TOKEN, initConfig, initModLog, saveLog, saveModLog, saveConfig
import time
# Import essential modules and config data.

# Create the Bot object which will be used to executive commands, events and run the discord bot.
bot = commands.Bot(command_prefix="?", help_command=None, intents=discord.Intents.all(), chunk_guilds_at_startup=False)