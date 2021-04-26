#!/usr/bin/python

import discord
from discord.utils import get
import os

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




class Discord(discord.Client):
    async def on_ready(self):
        myGuild = None
        for guild in self.guilds:
            if guild.name == GUILD:
                myGuild = guild

        print(
            f'{self.user} is connected to the following guild:\n'
            f'{myGuild.name}(id: {myGuild.id})'
        )

    async def on_member_join(self, member:discord.Member):
        welcome = get(member.guild.text_channels, name="welcome")
        rules = get(member.guild.text_channels,name="rules")
        suggestions = get(member.guild.text_channels,name="suggestions")
        roles = get(member.guild.text_channels, name='get-helper-roles')

        await member.send(f"Welcome {member.mention}! Check out the rules from the {rules.mention} channel. If you ever have any suggestions on how we can improve our server, you can freely put your opinions in the {suggestions.mention} channel. There is always a regular flow of memes through the instagram account (@the2020coder) and we also have Dank Memer in our server so there is never a lack of entertainment. You can also take help from or give help to your fellow coders in the server. If you wish to help then you can even sign up for a helper role from the {roles.mention} channel. Just react to the messaqge with an Emoji of your preferred language/tool and you are now a Helper!")
        await welcome.send(f"Welcome {member.mention}! Check out the rules from the {rules.mention} channel. We would love if you also folow our instagram account https://instagram.com/the2020coder.")

    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        if(payload.message_id==GETROLESMESSAGE):
            userrole = rolemap[payload.emoji.name]
            member = payload.member
            role = get(member.guild.roles, name=userrole)
            await member.add_roles(role)
            await member.send(f"Hello {member.mention}! You have been given the `{userrole}` Role in the server.")

    async def on_raw_reaction_remove(self, payload:discord.RawReactionActionEvent):
        if(payload.message_id==GETROLESMESSAGE):
            userrole = rolemap[payload.emoji.name]
            member = get(self.get_all_members() ,id=payload.user_id)
            role = get(member.guild.roles, name=userrole)
            await member.remove_roles(role)
            await member.send(f"Hello {member.mention}! You have been removed from the `{userrole}` Role in the server.")


intents = discord.Intents.default()
intents.members = True
intents.reactions = True


def run():
    client = Discord(intents=intents)
    client.run(TOKEN)

if __name__ == '__main__':
    run()