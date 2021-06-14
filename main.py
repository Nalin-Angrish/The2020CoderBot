#!/usr/bin/python
import sys
from dotenv import load_dotenv
load_dotenv()

# Define resource limits
if(sys.platform != "win32"):
	import resource
	_, hard = resource.getrlimit(resource.RLIMIT_NPROC)
	resource.setrlimit(resource.RLIMIT_NPROC, (5, hard))


from flask import Flask, request
import json

from ext.bot import TOKEN, client as bot
from ext.commands import Commands
from ext import instagram

import asyncio
from threading import Thread


app = Flask(__name__)
bot.add_cog(Commands(bot))
instagram.setup(bot)


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



def init():
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(TOKEN))
    Thread(target=loop.run_forever).start()


init()
if __name__ == "__main__":
    app.run(port=20202, host="0.0.0.0", debug=False)