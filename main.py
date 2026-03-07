from Utils.utilsLoader import *

@bot.event
async def on_guild_join(guild: discord.Guild):
    on_guild_join_func(guild)
@bot.event
async def on_guild_remove(guild: discord.Guild):
    on_guild_remove_func(guild)

bot.run(BOT_TOKEN)