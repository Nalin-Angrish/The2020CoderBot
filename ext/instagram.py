from discord import Embed
from discord.ext import commands
import _thread, time, requests, json, os, re

async def on_post_pic(bot:commands.Bot, post:dict):
	channel = bot.get_channel(799604699648360449)
	message = Embed(
		title=post["edge_media_to_caption"]["edges"][0]["node"]["text"].split("\n")[0]
		)
	message.set_image(url=post["display_url"])
	message.set_thumbnail(url=post["thumbnail_src"].replace("640x640", "150x150"))
	message.add_field(name="Like it now on Instagram!", value=f"https://www.instagram.com/p/{post['shortcode']}/")
	await channel.send(embed=message)
	print("Uploaded!")



def count_posts():
	url = 'https://www.instagram.com/accounts/login/'
	url_main = url + 'ajax/'
	auth = {
		'username': "the2020coder", 
		'enc_password': os.environ.get("INSTA_PASSWORD"),	# You will have to examine the XHR made while logging-in to get this encoded password. Then you can add this as an environment variable. 
		"queryparams": {},
		"optIntoOneTap":"false"
	}
	headers = {
		'referer': "https://www.instagram.com/accounts/login/",
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
	}

	with requests.Session() as s:
		s.headers.update(headers)
		req = s.get(url)
		csrftoken = re.findall('''"csrf_token":"(.*?)"''', req.text)[0]
		s.headers.update({'x-csrftoken': csrftoken})
		resp = s.post(url_main, data=auth, headers=headers)
		response = s.get("https://www.instagram.com/the2020coder/?__a=1")
	resp = json.loads(response.text)
	count = resp["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
	return resp, int(count)


def get_latest_post(data:dict):
	post = data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]
	return post





def check_post(bot:commands.Bot):
	if not os.path.exists("count.txt"):
		with open("count.txt", "w+") as f:
			f.write(str(count_posts()[1]))
	with open("count.txt", "r") as f:
		prev_num = int(f.read())
	while True:
		time.sleep(60) # wait a minute before checking again
		resp, num = count_posts()
		if num > prev_num:	# A picture was uploaded on Instagram
			post = get_latest_post(resp)
			print("The2020Coder uploaded a post on Instagram!")
			bot.dispatch("post_pic", bot=bot, post=post)
			print("Now posting it on Discord.")
			prev_num = num
			with open("count.txt", "w+") as f:
				f.write(str(num))

def setup(bot:commands.Bot):
	bot.add_listener(on_post_pic)
	_thread.start_new_thread(check_post,tuple([bot]))
	