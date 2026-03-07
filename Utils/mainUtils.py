import discord
from discord.ext import commands
from discord import app_commands, ui
import asyncio
import json

bot = commands.Bot(command_prefix="?", help_command=None, intents=discord.Intents.all(), chunk_guilds_at_startup=False)