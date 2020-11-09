import discord
from googlesearch import search

from user_defined import TOKEN_1, TOKEN_2
from get_period import period

token = str(TOKEN_1 + TOKEN_2)
my_results_list = []
client = discord.Client()  


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message):
	
	if "period?" == message.content.lower():
		if str(period()) != "Class time is over":
			await message.channel.send(f"```You will be having {period()[0]} for your {period()[1]} period.```")
		elif str(period()) == "Class time is over":
			await message.channel.send(f"```Class hours finished```")
		else:
			await message.channel.send(f'```syntax error```')
		
	if "hi!" == message.content.lower():
		await message.channel.send(f"Hello!! @{message.author}")
		
	if "alive?" == message.content.lower():
		await message.channel.send(f"Yes I am !! @{message.author}")
	
	if "tbh?" ==  message.content.lower():
		await message.channel.send(f"I am a bot which gives u info on ur class meets @{message.author}")
	
	if message.content.lower()[0] == '?':
		query = str(message.content.lower())[1:]
		
		for i in search(query): 
			results.append(i)
			await message.channel.send(f"```Result on query:{i}")


client.run(token)  
