from Utils.mainUtils import *

# Define on_guild_join/_leave
def on_guild_join(guild: discord.Guild):
    errors = []
    try:
        # Function from Utils/config.py, will add an entry of guild.id to the Databases/modlog.json file (if there is no entry yet).
        initModLog(guild.id)
    except Exception as e:
        # Add Exception to errors in case something goes wrong.
        errors.append(f"initModLog: {e}")
    try:
        # Function from Utils/config.py, will set the configuration of guild.id to default (if there is no entry yet).
        initConfig(guild.id)
    except Exception as e:
        # Same as above.
        errors.append(f"initConfig: {e}")
    # Create log to save in internal logs.
    log = {
        "type": "joinGuild",
        "guildId": guild.id,
        "errors": errors,
        "timestamp": int(f"{time.time():.0f}")
    }
    # Function from Utils/config.py, saves the log to Utils/log.json.
    saveLog(log)

def on_guild_remove(guild: discord.Guild):
    # Works just like on_guild_join (without the initModLog function).
    # Modlogs and Config will not be deleted upon bot removal/rejoin. initModLog and initConfig ignore guilds with previous logs/configs.
    errors = []
    log = {
        "type": "leaveGuild",
        "guildId": guild.id,
        "errors": errors,
        "timestamp": int(f"{time.time():.0f}")
    }
    saveLog(log)