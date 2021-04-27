#!/usr/bin/python

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
load_dotenv()
import os
from ext.commands import Commands
from ext import instagram

TOKEN = os.environ.get("BOT_TOKEN")
GUILD = "the2020coder"
GETROLESMESSAGE = 801056866289451008
rolemap = {
    "python": "Python Helper",
    "java": "Java Helper",
    "javascript": "JavaScript Helper",
    "html": "HTML Helper",
    "css": "CSS Helper",
    "git": "Git Helper",
    "terminal": "Terminal Helper"
}


intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix=commands.when_mentioned_or('code '), intents=intents)


@client.event
async def on_ready():
    myGuild = None
    for guild in client.guilds:
        if guild.name == GUILD:
            myGuild = guild

    print(f'{client.user} is connected to {myGuild.name}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The2020Coder's Discord Server"), status=discord.Status.online)



@client.event
async def on_member_join(member:discord.Member):
    welcome = get(member.guild.text_channels, name="welcome")
    rules = get(member.guild.text_channels,name="rules")
    suggestions = get(member.guild.text_channels,name="suggestions")
    roles = get(member.guild.text_channels, name='get-helper-roles')

    await member.send(f"Welcome {member.mention}! Check out the rules from the {rules.mention} channel. If you ever have any suggestions on how we can improve our server, you can freely put your opinions in the {suggestions.mention} channel. There is always a regular flow of memes through the instagram account (@the2020coder) and we also have Dank Memer in our server so there is never a lack of entertainment. You can also take help from or give help to your fellow coders in the server. If you wish to help then you can even sign up for a helper role from the {roles.mention} channel. Just react to the messaqge with an Emoji of your preferred language/tool and you are now a Helper!")
    await welcome.send(f"Welcome {member.mention}! Check out the rules from the {rules.mention} channel. We would love if you also folow our instagram account https://instagram.com/the2020coder.")



@client.event
async def on_raw_reaction_add(payload:discord.RawReactionActionEvent):
    if(payload.message_id==GETROLESMESSAGE):
        userrole = rolemap[payload.emoji.name]
        member = payload.member
        role = get(member.guild.roles, name=userrole)
        await member.add_roles(role)
        await member.send(f"Hello {member.mention}! You have been given the `{userrole}` Role in the server.")



@client.event
async def on_raw_reaction_remove(payload:discord.RawReactionActionEvent):
    if(payload.message_id==GETROLESMESSAGE):
        userrole = rolemap[payload.emoji.name]
        member = get(client.get_all_members() ,id=payload.user_id)
        role = get(member.guild.roles, name=userrole)
        await member.remove_roles(role)
        await member.send(f"Hello {member.mention}! You have been removed from the `{userrole}` Role in the server.")


if __name__ == "__main__":
    client.add_cog(Commands(client))
    instagram.setup(client)
    client.run(TOKEN)