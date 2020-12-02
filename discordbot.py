import discord
from googlesearch import search

from user_defined import TOKEN_1, TOKEN_2
from get_period import sprd
from get_period import period

from quotes import quote
from quotes import rand_no, data

from time import sleep
import arrow
current_time = str(arrow.now('Asia/Calcutta').format('hh:mm:A'))
time_elements = current_time.split(':')

def ret_obj_h(time):
	req_time = arrow.get(time, 'h')
	return req_time

def ret_obj(time):
	req_time = arrow.get(time, 'h:m')
	return req_time

def ret_obj_a(time):
	req_time = arrow.get(time, 'A')
	return req_time



hour = arrow.get(time_elements[0], 'h')
minute = arrow.get(time_elements[1], 'm')
meridian = arrow.get(time_elements[2], 'A')
h_m = arrow.get(time_elements[0] + ':' + time_elements[1], 'h:m') 
token = str(TOKEN_1 + TOKEN_2)
results = []
client = discord.Client()  


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message):
	
	if "period?" == message.content.lower():
			
			await message.channel.send(f"```You will be having {period()[0]} for your {period()[1]} period.```")
		
			
		
		
		
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
	if message.content.lower() == '.q'and (str(message.author).strip() == 'iSimpYT_#3772' or str(message.author).strip() == 'iSimpYT_#8601' ):
			await message.channel.send(f"```[User Spamming Reported] [You can use this command after 785 Days]```")

	if message.content.lower() == '.q'and (str(message.author).strip() != 'iSimpYT_#3772' or str(message.author).strip() != 'iSimpYT_#8601' ):
			quote_tup = quote(rand_no, data)
			await message.channel.send(f"```{quote_tup[0]}\n\n-- {quote_tup[1]}```")
			


		
			
		
					
		
client.run(token)  
