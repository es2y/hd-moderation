from Utils.mainUtils import *

def on_guild_join(guild: discord.Guild):
    errors = []
    try:
        initModLog(guild.id)
    except Exception as e:
        errors.append(f"initModLog: {e}")
    log = {
        "type": "joinGuild",
        "guildId": guild.id,
        "errors": errors,
        "timestamp": int(f"{time.time():.0f}")
    }
    saveLog(log)

def on_guild_remove(guild: discord.Guild):
    errors = []
    log = {
        "type": "leaveGuild",
        "guildId": guild.id,
        "errors": errors,
        "timestamp": int(f"{time.time():.0f}")
    }
    saveLog(log)