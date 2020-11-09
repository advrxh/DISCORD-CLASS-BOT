import discord

from user_defined import TOKEN_1, TOKEN_2
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
			await message.channel.send(f"Yes I am !! @{message.author}")
			i = 1





client.run(TOKEN_1 + TOKEN_2)  
