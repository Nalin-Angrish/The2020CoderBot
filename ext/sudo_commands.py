import discord
from discord.ext import commands
from discord.utils import get
from ._utils import allcases
from typing import Optional
from time import sleep
import asyncio
import inspect


class SudoCommands(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		self.bot.remove_command("help")
		self.prefixes = allcases("sudo ")

	async def cog_check(self, ctx):
		if(ctx.prefix not in self.prefixes): return False
		if(get(ctx.guild.roles, name="Administrators") not in ctx.message.author.roles):
			await ctx.send(f"Cannot use `sudo` because user {ctx.message.author.mention} does not have the required priveledges.")
			return False
		return True
	
	@commands.command(name="kick", help="Kick a User")
	async def kick(self, ctx, member: Optional[discord.Member] = None):
		if(member):
			await ctx.send(f"Kicking User {member.mention} in 5 seconds...")
			sleep(5)
			await ctx.send(f"B-Bye {member.mention}!")
			await member.kick()
		else:
			await ctx.send("Please specify a user to kick.")

	@commands.command(name="ban", help="Ban a User")
	async def ban(self, ctx, member: Optional[discord.Member] = None):
		if(member):
			await ctx.send(f"Are you sure you want to ban {member.mention} and not kick? This might be dangerous. (Y/N)")
			try:
				def check(msg):
					return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower()[0] in ["y", "n"]
				msg = await self.bot.wait_for("message", check=check, timeout=10) # 10 seconds to reply
				msg = msg.content.lower()
				if msg.startswith("y"):
					await ctx.send(f"B-Bye {member.mention}!")
					#await member.ban()
				elif msg.startswith("n"):
					await ctx.send("Okay...")
				else:
					await ctx.send(f"Unknown response {msg}")
			except asyncio.TimeoutError:
				await ctx.send("No reply so ignoring...")
		else:
			await ctx.send("Please specify a user to ban.")
	
	@commands.command(name="commands", help="Display this message.")
	async def commands(self, ctx):
		message = "```Sudo Commands (Only for admins): \n"
		for func in SudoCommands.__dict__:
			if func.startswith("_") or func=="cog_check":
				continue
			function = SudoCommands.__dict__[func]
			args = inspect.getmembers(function)
			args = list(args[3][1]["params"])[2:]
			if len(args)==0:
				args = None
			else:
				fargs = ""
				for arg in args:
					fargs += f" <{arg}>"
				args = fargs
			message += f"    sudo {function.__dict__['name']}{args if args else ''}: {function.__dict__['help']}\n"
		message += "```"
		await ctx.send(message)
		self.kick