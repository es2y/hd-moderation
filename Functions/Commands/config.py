from Utils.mainUtils import *

async def config(cmd: discord.Interaction):
    # Check if the user has administrator permissions.
    if not cmd.user.guild_permissions.administrator:
        # If not, send a message and stop the function.
        await cmd.response.send_message(f":x: Not authorized.", ephemeral=True)
        return

    # Create message embed.
    embed1 = discord.Embed(
        title=f"Server Config | {cmd.guild.name}",
        description="Select a configuration type...",
        color=0x00ffff
    )

    # Create views to add buttons for configuration.
    basicView = ui.View(timeout=None)

    permissions = ui.Button(label="Moderation Permissions", style=discord.ButtonStyle.blurple)
    
    async def permissionsCallback(permsCb: discord.Interaction):
        if permsCb.user != cmd.user:
            await permsCb.response.send_message("You are not allowed to use this.")
            return
        muteRoles = configDb[str(permsCb.guild.id)]["permissions"]["timeout"]
        banRoles = configDb[str(permsCb.guild.id)]["permissions"]["ban"]
        kickRoles = configDb[str(permsCb.guild.id)]["permissions"]["kick"]
        modlogRoles = configDb[str(permsCb.guild.id)]["permissions"]["modlogs"]

        def formatRoleList(role_list):
            new_role_list = [f"<@&{role}>" for role in role_list]
            if len(new_role_list) > 3:
                rolelistLen = len(new_role_list)
                text = ", ".join(new_role_list[:3])
                text += f" +{rolelistLen-3}"
            else:
                text = ", ".join(new_role_list)
            if new_role_list == []:
                text = "None"
            
            return text
        
        muteRoles = formatRoleList(muteRoles)
        banRoles = formatRoleList(banRoles)
        kickRoles = formatRoleList(kickRoles)
        modlogRoles = formatRoleList(modlogRoles)

        embed2 = discord.Embed(
            title="Server Config | Permissions",
            description=f"Timeout Members: {muteRoles}\nKick Members: {kickRoles}\nBan Members: {banRoles}\nView Modlogs: {modlogRoles}\n\nAdministrator roles automatically have all permissions.",
            color=0x00ffff
        )

        newView = ui.View(timeout=None)
        goback = ui.Button(label="Back", style=discord.ButtonStyle.gray)

        async def backCallback(backCb: discord.Interaction):
            if backCb.user != permsCb.user:
                await backCb.response.send_message("You are not allowed to use this.")
                return
            await cmd.edit_original_response(embed=embed1, view=basicView)
            await backCb.response.defer(thinking=False)

        goback.callback = backCallback
        newView.add_item(goback)
        await cmd.edit_original_response(embed=embed2, view=newView)
        await permsCb.response.defer(thinking=False)

    permissions.callback = permissionsCallback
    basicView.add_item(permissions)

    await cmd.response.send_message(embed=embed1, view=basicView)