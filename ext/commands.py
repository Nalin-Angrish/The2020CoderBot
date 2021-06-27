import discord
from discord.ext import commands
from .bot import BOTCHATCHANNEL, RULESCHANNEL, rolemap
from ._utils import allcases


class Commands(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		self.bot.remove_command("help")
		self.prefixes = allcases("code ")
	async def cog_check(self, ctx):
		return ctx.prefix in self.prefixes
	
	@commands.command(name="rules", help="Tell the rules of the server.")
	async def rules(self, ctx):
		rules = self.bot.get_channel(RULESCHANNEL)
		await ctx.send(f"The rules for the server are mentioned in the {rules.mention} channel. To summarize:\n```Discrimination, Bullying and Harassing is strictly prohibited. Self promotion without the consent of an Administrator is not allowed. Spamming or toxic swearing is considered inappropriate and should be taken care of.```\nLogical extensions of rules may also be enforced.")

	@commands.command(name="help", help="Display this message.")
	async def help(self, ctx):
		message = "```Commands: \n"
		for func in Commands.__dict__:
			if func.startswith("_") or func=="cog_check":
				continue
			function = Commands.__dict__[func]
			message += f"    code {function.__dict__['name']}: {function.__dict__['help']}\n"
		message += "```"
		await ctx.send(message)

	@commands.command(name="insta", help="Get the link of The2020Coder's Instagram account")
	async def insta(self, ctx):
		await ctx.send("Check out some awesome memes by The2020Coder on Instagram!\nhttps://www.instagram.com/the2020coder")

	@commands.command(name="git", help="Get The2020CoderBot's source code on GitHub")
	async def git(self, ctx):
		await ctx.send("Collaborate on The2020CoderBot on GitHub!\nhttps://github.com/Nalin-2005/The2020CoderBot")

	@commands.command(name="invite", help="Generate an invite link for this server.")
	async def invite(self, ctx):
		await ctx.send("You can use this link to invite your friends to this server:\nhttps://discord.gg/DekWAGD3EF")

	@commands.command(name="chat", help="Get information about The2020CoderBot's chat features")
	async def chat(self, ctx):
		channel_chat = self.bot.get_channel(BOTCHATCHANNEL)
		message = f"The2020CoderBot runs a Deep Learning model using Tensorflow which helps it to respond to user messages. To chat with me, you can visit the {channel_chat.mention} channel, or message me in my DM. If you wish to type messages which i should ignore, prefix the messages with a '!'. If you wish to improve my intelligence, you can work on my code on GitHub."
		await ctx.send(message)

	@commands.command(name="stats", help="Get the current Server stats.")
	async def stats(self, ctx):
		guild:discord.Guild = ctx.guild
		members:list[discord.Member] = await guild.fetch_members().flatten()
		helper_roles = rolemap.values()

		userno = len(members)
		botno = len([member for member in members if member.bot])
		helpers = []
		for member in members:
			for role in member.roles:
				if role.name in helper_roles and member not in helpers:
					helpers.append(member)
		helperno = len(helpers)

		resp =  f"""\
Guild `{guild.name}`'s stats:
  Number of Humans: {userno-botno}
  Number of Bots: {botno}
  Number of Helpers: {helperno}\
"""
		await ctx.send(resp)