"""
Tiny bot that removes a harmony role if a user gets assigend a role 
from a list of team-roles.
"""

import discord

token = 'NTEwNTcwNDg4NTk5MjgxNjg1.DsuQ6A.ZGu4re7pzh_iy1vxmVJc5HaH73Y'

client = discord.Client()

team_role_names = {"mystic","valor","instinct"}

@client.event
async def on_member_update(before, after):
    "Removes the role harmony if user got a team role."
    harmony_role = next(r for r in after.guild.roles if r.name == 'harmony')
    team_roles = {r for r in after.guild.roles if r.name in team_role_names}
    added_roles = {*after.roles} - {*before.roles}
    if added_roles.intersection(team_roles):
        await after.remove_roles(harmony_role)


client.run(token)
