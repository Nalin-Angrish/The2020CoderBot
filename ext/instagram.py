from discord import Embed
from discord.ext import commands
from flask import Flask, request
import json, _thread

async def on_post_pic(bot:commands.Bot, post:dict):
	channel = bot.get_channel(799604699648360449)
	message = Embed(
		title=post["caption"].split("*-*-*")[0]
		)
	message.set_image(url=post["image"])
	message.set_thumbnail(url=post["image"])
	message.add_field(name="Like it now on Instagram!", value=post["url"])
	await channel.send(embed=message)
	print("Uploaded!")




def check_post(bot:commands.Bot):
	app = Flask(__name__)

	@app.route("/")
	def index():
		return "Hello World!"

	@app.route("/instagram_pic_posted")
	def onPost():
		data = request.get_data().decode().replace("\n", "*-*-*")
		data = json.loads(data)
		print("The2020Coder uploaded a post on Instagram!")
		bot.dispatch("post_pic", bot=bot, post=data)
		print("Now posting it on Discord.")
		return "Thanks!"

	app.run(port=20202, host="0.0.0.0", debug=False)




def setup(bot:commands.Bot):
	bot.add_listener(on_post_pic)
	_thread.start_new_thread(check_post,tuple([bot]))
	