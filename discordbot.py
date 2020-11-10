import discord
from googlesearch import search

from user_defined import TOKEN_1, TOKEN_2
from get_period import sprd
from get_period import period

from time import sleep
import arrow
current_time = str(arrow.now('Asia/Calcutta').format('hh:mm:A'))
time_elements = current_time.split(':')

hour = time_elements[0]
minute = time_elements[1]
meridian = time_elements[2]

token = str(TOKEN_1 + TOKEN_2)
results = []
client = discord.Client()  


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message):
	
	if "period?" == message.content.lower():
		if int(hour) > 08 and int(hour) < 12 and meridian == 'AM':
			await message.channel.send(f"```You will be having {period()[0]} for your {period()[1]} period.```")
		elif int(hour) > 12 and int(hour) < 08 and meridian == 'AM':
			await message.channel.send(f"```Not at the moment in few hours or minutes.```")
		else:
			await message.channel.send(f'```Class hours have been finished```')
		
	if "!hi" == message.content.lower():
		await message.channel.send(f"Hello!! @{message.author}")
		
	if "?alive" == message.content.lower():
		await message.channel.send(f"Yes I am !! @{message.author}")
	
	if "?tbh" ==  message.content.lower():
		await message.channel.send(f"I am a bot which gives u info on ur class meets @{message.author}")
	
	if message.content.lower()[0:2] == '?g':
		query = str(message.content.lower())[1:]
		
		for i in search(query, num_results=3): 
			results.append(i)
			await message.channel.send(f"```Result on {query} @{message.author}:```{i}")
	
		
	if message.content.lower()[0:2] == '?p':
		args = str(message.content.lower()[3:]).split(' ')
		day_ = args[0].title()
		prd_ = int(args[1])
		day_obj = arrow.get(day_, 'ddd').format('dddd')
		period_req = sprd(day_, prd_)
		await message.channel.send(f"``` You will be having {period_req} ```")
		sleep(1)
		
	

		


client.run(token)  
