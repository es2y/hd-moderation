from Utils.utilsLoader import *
# Import everything from other files in one single line.

# Connect the on_guild_join/_remove to the previously defined functions.
@bot.event
async def on_guild_join(guild: discord.Guild):
    on_guild_join_func(guild)
@bot.event
async def on_guild_remove(guild: discord.Guild):
    on_guild_remove_func(guild)

# Run the bot with all connected commands and events.
bot.run(BOT_TOKEN)