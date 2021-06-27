#!/usr/bin/python

import discord
from discord.ext import commands
from discord.utils import get
import os
from ._utils import *
from .chat import predict

TOKEN = os.environ.get("BOT_TOKEN")
GUILD = "The2020Coder"
GETROLESMESSAGE = 801056866289451008
BOTCHATCHANNEL = 852110126940815371
RULESCHANNEL = 799605853044604938
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
intents.messages = True

client = commands.Bot(command_prefix=allcases("code ")+allcases("sudo "), intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is ready to Rock!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="code help"), status=discord.Status.online)



@client.event
async def on_member_join(member:discord.Member):
    welcome = get(member.guild.text_channels, name="welcome")
    rules = get(member.guild.text_channels,name="rules")
    suggestions = get(member.guild.text_channels,name="suggestions")
    roles = get(member.guild.text_channels, name='get-helper-roles')

    await welcome.send(f"Welcome {member.mention}! Check out the rules from the {rules.mention} channel. We would love if you also folow our instagram account https://instagram.com/the2020coder.")
    await member.send(f"Welcome {member.mention}! Check out the rules from the {rules.mention} channel. If you ever have any suggestions on how we can improve our server, you can freely put your opinions in the {suggestions.mention} channel. There is always a regular flow of memes through the instagram account (@the2020coder) and we also have Dank Memer in our server so there is never a lack of entertainment. You can also take help from or give help to your fellow coders in the server. If you wish to help then you can even sign up for a helper role from the {roles.mention} channel. Just react to the messaqge with an Emoji of your preferred language/tool and you are now a Helper!")


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


@client.event
async def on_message(message:discord.Message):
    await client.process_commands(message)
    if (message.author != client.user) and ((message.channel.id == BOTCHATCHANNEL) or isinstance(message.channel, discord.channel.DMChannel)) and (not isCommand(message.content)) and (not isIgnored(message.content)):
        response = predict(message.content)
        if response:
            response, embed = format_info(response, message, client)
            if(embed):
                await message.reply(embed=response)
            else:
                await message.reply(response)