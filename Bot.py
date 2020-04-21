import os
import discord
from discord.ext import commands

class CompileDis(commands.Bot):
	def __init__(self,token):
		self.token = token
		super().__init__(command_prefix=';run')
		self.load_cogs()

	def load_cogs(self):
		extensions = ['cogs.admin']

		for extension in extensions:
			try:
				self.load_extension(extension)
			except Exception as error:
				print(f'{extension} cannot be loaded: {error}')
		pass

	async def on_ready(self):
		print(f'Logged in as {self.user.name} {self.user.id}')
		await self.change.presence(status=discord.Status.online)


	def run(self):
		super().run(self.token)