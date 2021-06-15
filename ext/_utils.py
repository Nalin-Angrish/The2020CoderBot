import discord
from discord import Embed
import cloudscraper

NALIN_ID = 747752916177387591
HELP_ID = 799605375225430067
JOKES_API = "https://v2.jokeapi.dev/joke/"
MEME_API = "https://meme-api.herokuapp.com/gimme"
scraper = cloudscraper.create_scraper()


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

def format_info(into: str, _input:discord.Message, bot:discord.Client):
    message = into
    embed = False
    if (r"{8ball}" in message):
        message = ""
    if (r"{nalin}" in message):
        nalin = bot.get_user(NALIN_ID)
        message = message.replace(r"{nalin}", nalin.mention)
    if (r"{user}" in message):
        message = message.replace(r"{user}", _input.author.mention)
    if (r"{help}" in message):
        channel = bot.get_channel(HELP_ID)
        message = message.replace(r"{help}", channel.mention)
    if (r"{joke}" in message):
        joke_data = scraper.get(JOKES_API+"Any").json()
        if joke_data['type'] == "twopart":
            joke = joke_data["setup"] + "\n**" + joke_data["delivery"] + "**"
        elif joke_data['type'] == "single":
            joke = joke_data["joke"] + "\n**"
        message = message.replace(r"{joke}", joke)
    if (r"{pjoke}" in message):
        joke_data = scraper.get(JOKES_API+"Programming").json()
        if joke_data['type'] == "twopart":
            joke = joke_data["setup"] + "\n**" + joke_data["delivery"] + "**"
        elif joke_data['type'] == "single":
            joke = joke_data["joke"] + "\n**"
        message = message.replace(r"{pjoke}", joke)
    if (r"{dark-joke}" in message):
        joke_data = scraper.get(JOKES_API+"Dark").json()
        if joke_data['type'] == "twopart":
            joke = joke_data["setup"] + "\n**" + joke_data["delivery"] + "**"
        elif joke_data['type'] == "single":
            joke = joke_data["joke"] + "\n**"
        message = message.replace(r"{dark-joke}", joke)
    if (r"{pun}" in message):
        joke_data = scraper.get(JOKES_API+"Pun").json()
        if joke_data['type'] == "twopart":
            joke = joke_data["setup"] + "\n**" + joke_data["delivery"] + "**"
        elif joke_data['type'] == "single":
            joke = joke_data["joke"] + "\n**"
        message = message.replace(r"{pun}", joke)
    if (r"{meme}" in message):
        nsfw = True
        while(nsfw):
            meme_data = scraper.get(MEME_API).json()
            nsfw = meme_data["nsfw"]
        meme = meme_data
        title = message.replace(r"{meme}", "")
        message = Embed(title=title)
        message.set_image(url=meme["preview"][-1])
        message.add_field(name=meme['title'], value=meme["postLink"])
        embed = True
    return message, embed

def isIgnored(text:str):
    return text.startswith("!")
