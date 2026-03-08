from Utils.mainUtils import *

async def config(cmd: discord.Interaction):
    if not cmd.user.guild_permissions.administrator:
        await cmd.response.send_message(f":x: Not authorized.", ephemeral=True)
        return
    
    await cmd.response.send_message(f":x: This command is currently under development. You can find updates on [the bot's github page](<https://github.com/es2y/hd-moderation>).", ephemeral=True)
    return