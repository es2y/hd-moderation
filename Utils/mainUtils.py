import discord
from discord.ext import commands
from discord import app_commands, ui
import asyncio
import json
from Utils.config import *
import time

bot = commands.Bot(command_prefix="?", help_command=None, intents=discord.Intents.all(), chunk_guilds_at_startup=False)