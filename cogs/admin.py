import discord
from discord.ext import commands

def setup(bot):
	bot.add_cog(Commands(bot))

class Commands:
	def __init__(self,bot):
		self.bot = bot


	@commands.command()

	async def purge(self,ctx,amount=5):
		'''
		[prefix]purge A removes A messages.
		'''
		channel = ctx.message.channel
		messages = []

		async for message in ctx.history(limit=amount+1):
			messages.append(message)

		await channel.delete_messages(messages)
		await ctx.send(f'{amount} messages were deleted.')

	async def commitNotAlive(self,ctx):
		await self.bot.close()