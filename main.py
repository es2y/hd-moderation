from Utils.utilsLoader import *
# Import everything from other files in one single line.

# Connect the on_guild_join/_remove to the previously defined functions.
@bot.event
async def on_guild_join(guild: discord.Guild):
    on_guild_join_func(guild)
@bot.event
async def on_guild_remove(guild: discord.Guild):
    on_guild_remove_func(guild)

@bot.event
async def on_ready():
    print("Syncing bot tree.")
    await bot.tree.sync()
    print("Synced.")

@bot.tree.command(name="config", description="View and update the bot's config.")
async def config(interaction: discord.Interaction):
    await config_func(interaction)

# Run the bot with all connected commands and events.
bot.run(BOT_TOKEN)