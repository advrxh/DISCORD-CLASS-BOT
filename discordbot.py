import discord

from user_defined import TOKEN
from get_period import period

client = discord.Client()  


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}')  


@client.event
async def on_message(message):
	i = 0
	while i < 1:
		if "period?" == message.content.lower():
			await message.channel.send(f"```You will be having {period()[0]} for your {period()[1]} period.```")
			i = 1
		if "hi!" == message.content.lower():
			await message.channel.send(f"Hello!! @{message.author}")
			i = 1
		if "alive?" == message.content.lower():
			await message.channel.send(f"Yes I am!! @{message.author}")
			i = 1





client.run(TOKEN)  
