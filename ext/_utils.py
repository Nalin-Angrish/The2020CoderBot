import discord
from discord import Embed
import requests


NALIN_ID = 747752916177387591
HELP_ID = 799605375225430067
JOKES_API = "https://official-joke-api.appspot.com/random_joke"
PJOKES_API = "https://official-joke-api.appspot.com/jokes/programming/random"
MEME_API = "https://meme-api.herokuapp.com/gimme"


def allcases(string):
    n = len(string)
    mx = 1 << n
    inp = string.lower()
    allcombs = []
      
    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()
   
        temp = ""
        for i in combination:
            temp += i
        allcombs.append(temp)
    return allcombs

def isCommand(message:str):
    starts = allcases("code ")
    status = False
    for start in starts:
        if(message.startswith(start)):
            status = True
    return status

def format_info(into:str, _input:discord.Message, bot:discord.Client):
    message = into
    embed = False
    if (r"{nalin}" in message):
        nalin = bot.get_user(NALIN_ID)
        message = message.replace(r"{nalin}", nalin.mention)
    if (r"{user}" in message):
        message = message.replace(r"{user}", _input.author.mention)
    if (r"{help}" in message):
        channel = bot.get_channel(HELP_ID)
        message = message.replace(r"{help}", channel.mention)
    if (r"{joke}" in message):
        joke_type = "programming"
        while(joke_type=="programming"):
            joke_data = requests.get(JOKES_API).json()
            joke_type = joke_data["type"]
        joke = joke_data["setup"] + "\n**" + joke_data["punchline"] + "**"
        message = message.replace(r"{joke}", joke)
    if (r"{pjoke}" in message):
        joke_data = requests.get(PJOKES_API).json()[0]
        joke = joke_data["setup"] + "\n**" + joke_data["punchline"] + "**"
        message = message.replace(r"{pjoke}", joke)
    if (r"{meme}" in message):
        nsfw = True
        while(nsfw):
            meme_data = requests.get(MEME_API).json()
            nsfw = meme_data["nsfw"]
        meme = meme_data
        title = message.replace(r"{meme}", "")
        message = Embed(
		    title=title
		)
        message.set_image(url=meme["preview"][-1])
        message.add_field(name=f"/r/{meme['subreddit']}", value=meme["postLink"])
        embed = True
    return message, embed

def isIgnored(text:str):
    return text.startswith("!")