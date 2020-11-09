import discord

from user_defined import TOKEN_1, TOKEN_2
from get_period import period

token = str(TOKEN_1 + TOKEN_2)
client = discord.Client()  


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message):
	
	if "period?" == message.content.lower():
		await message.channel.send(f"```You will be having {period()[0]} for your {period()[1]} period.```")
		
	if "hi!" == message.content.lower():
		await message.channel.send(f"Hello!! @{message.author}")
		
	if "alive?" == message.content.lower():
		await message.channel.send(f"Yes I am !! @{message.author}")
	
	if "tbh?" ==  message.content.lower():
		await message.channel.send(f"I am a bot which gives u info on ur class meets @{message.author}")
	

client.run(token)  
