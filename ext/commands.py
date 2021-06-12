from discord.ext import commands
from discord.utils import get
from discord import Embed

from .bot import BOTCHATCHANNEL


class Commands(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		self.bot.remove_command("help")
	
	@commands.command(name="rules", help="Tell the rules of the server.")
	async def rules(self, ctx):
		rules = get(ctx.guild.text_channels,name="rules")
		await ctx.send(f"The rules for the server are mentioned in the {rules.mention} channel. To summarize:\n```Discrimination, Bullying and Harassing is strictly prohibited. Self promotion without the consent of an Administrator is not allowed. Spamming or toxic swearing is considered inappropriate and should be taken care of.```\nLogical extensions of rules may also be enforced.")

	@commands.command(name="help", help="Display this message.")
	async def help(self, ctx):
		message = "```Commands: \n"
		for func in Commands.__dict__:
			if func.startswith("_"):
				continue
			function = Commands.__dict__[func]
			message += "    code " + function.__dict__["name"] + ": " + function.__dict__["help"] + "\n"
		message += "```"
		await ctx.send(message)

	@commands.command(name="insta", help="Get the link of The2020Coder's Instagram account")
	async def insta(self, ctx):
		message = Embed(title="Click to check out The2020Coder on Instagram!",type="link", url="https://www.instagram.com/the2020coder")
		message.set_image(url="https://instagram.fixc6-1.fna.fbcdn.net/v/t51.2885-19/s320x320/123509246_175040474221222_3294715054928130681_n.jpg?tp=1&_nc_ht=instagram.fixc6-1.fna.fbcdn.net&_nc_ohc=UatFWX7hQzgAX-v_Wqn&edm=ABfd0MgAAAAA&ccb=7-4&oh=981633458ae03673e3ae29dfb9c1110b&oe=60AAE7E1&_nc_sid=7bff83")
		await ctx.send(embed=message)

	@commands.command(name="git", help="Get The2020CoderBot's source code on GitHub")
	async def git(self, ctx):
		await ctx.send("Collaborate on The2020CoderBot on GitHub!\nhttps://github.com/Nalin-2005/The2020CoderBot")

	@commands.command(name="chat", help="Get information about The2020CoderBot's chat features")
	async def chat(self, ctx):
		channel_chat = self.bot.get_channel(BOTCHATCHANNEL)
		message = f"The2020CoderBot runs a Deep Learning model using Tensorflow which helps it to respond to user messages. To chat with me, you can visit the {channel_chat.mention} channel, or message me in my DM. If you wish to type messages which i should ignore, prefix the messages with a '!'. If you wish to improve my intelligence, you can work on my code on GitHub."
		ctx.send(message)