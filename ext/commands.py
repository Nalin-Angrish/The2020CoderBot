from discord.ext import commands
from discord.utils import get
from discord import Embed

class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.bot.remove_command("help")
	
	@commands.command(name="rules", help="Tell the rules of the server.", case_insensitive=True)
	async def rules(self, ctx):
		rules = get(ctx.guild.text_channels,name="rules")
		await ctx.send(f"The rules for the server are mentioned in the {rules.mention} channel. To summarize:\n```Discrimination, Bullying and Harassing is strictly prohibited. Self promotion without the consent of an Administrator is not allowed. Spamming or toxic swearing is considered inappropriate and should be taken care of.```\nLogical extensions of rules may also be enforced.")

	@commands.command(name="help", help="Display this message.", case_insensitive=True)
	async def help(self, ctx):
		message = "```Commands: \n"
		for func in Commands.__dict__:
			if func.startswith("_"):
				continue
			function = Commands.__dict__[func]
			message += "    code " + function.__dict__["name"] + ": " + function.__dict__["help"] + "\n"
		message += "```"
		await ctx.send(message)

	@commands.command(name="insta", help="Get the link of The2020Coder's Instagram account", case_insensitive=True)
	async def insta(self, ctx):
		message = Embed(title="Click to check out The2020Coder on Instagram!",type="link", url="https://www.instagram.com/the2020coder")
		message.set_image(url="https://instagram.fixc6-1.fna.fbcdn.net/v/t51.2885-19/s320x320/123509246_175040474221222_3294715054928130681_n.jpg?tp=1&_nc_ht=instagram.fixc6-1.fna.fbcdn.net&_nc_ohc=UatFWX7hQzgAX-v_Wqn&edm=ABfd0MgAAAAA&ccb=7-4&oh=981633458ae03673e3ae29dfb9c1110b&oe=60AAE7E1&_nc_sid=7bff83")
		await ctx.send(embed=message)

	@commands.command(name="instagram", help="Same as \"code insta\"", case_insensitive=True)
	async def instagram(self, ctx):
		await self.insta(ctx)