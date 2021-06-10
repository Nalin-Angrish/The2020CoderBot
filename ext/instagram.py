from discord import Embed
from discord.ext import commands

async def on_post_pic(bot:commands.Bot, post:dict):
	channel = bot.get_channel(799604699648360449)
	message = Embed(
		title=post["caption"].split("*-*-*")[0]
		)
	message.set_image(url=post["image"])
	message.add_field(name="Like it now on Instagram!", value=post["url"])
	await channel.send(embed=message)
	print("Uploaded!")


def setup(bot:commands.Bot):
	bot.add_listener(on_post_pic)