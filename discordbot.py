import discord
from googlesearch import search

from user_defined import TOKEN_1, TOKEN_2
from get_period import sprd
from get_period import period

from studentProfileHandler import ReturnPortionsSpecific

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

client.command_prefix = '.'


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message):
	# print(message.author.display_name)
	
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


	# if message.content.lower() == '.createprfl' :

	# 	name = message.author.display_name.replace(' ', '_')

	# 	if message.content.lower() == '.createprfl':
	# 		if CheckStudentExistence(name = name):
	# 			embed = discord.Embed(title = f'Student Profile for {message.author.display_name} Exists', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
	# 			description = f'Profile Exists', color = 0xCF0A0E)

	# 			await message.channel.send(embed = embed)

	# 		else:
	# 			createStudent(name = name, description = None)
	# 			embed = discord.Embed(title = f'Creating Student Profile for {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
	# 			description = f'Sucessfully Created Profile for {message.author.display_name}', color = 0x5cf2fa)
	# 			await message.channel.send(embed = embed)

	# 	elif message.content.lower()[:15] == '.createprfl -d' :
	# 		description = message.content[15:]
	# 		if CheckStudentExistence(name = name):
	# 			embed = discord.Embed(title = f'Student Profile for {message.author.display_name} Exists', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
	# 			description = f'Profile Exists', color = 0xCF0A0E)

	# 			await message.channel.send(embed = embed)

	# 		else:
	# 			createStudent(name = name, description = description)

	# 			embed = discord.Embed(title = f'Creating Student Profile for {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
	# 			description = f'Sucessfully Created Profile for {message.author.display_name}', color = 0x5cf2fa)

	# 			await message.channel.send(embed = embed)
	
	#maths

	if message.content.lower() == "-m":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('mathematics').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Mathematics Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)
	
	#chem
	if message.content.lower() == "-c":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('chemistry').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Chemistry Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)
	
	#bio
	if message.content.lower() == "-b":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('biology').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Biology Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)
	#phy
	if message.content.lower() == "-p":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('physics').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Physics Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)


	#history
	if message.content.lower() == "-h":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('history').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'History Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)

	#economics

	if message.content.lower() == "-e":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('economics').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Economics Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)

	#geo
	if message.content.lower() == "-g":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('geography').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Geography Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)
	#civics
	if message.content.lower() == "-ci":
		portions = str()
		portions_list = list(ReturnPortionsSpecific('civics').values())
		

		for i, j  in enumerate(portions_list):
			portions += f"Lesson {i+1} : {j}\n" 

		embed = discord.Embed(title = f'Civics Portions requested by {message.author.display_name}', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = f'{portions}', color = 0xCF0A0E)
		await message.channel.send(embed = embed)
	if message.content.lower() == '!help -s':

		description = "Mathematics : `-m`\nChemistry : `-c`\nBiology : `-b`\nPhysics : `-p`\nHistory : `-h`\nEconomics : `-e`\nGeography : `-g`\nCivics : `-ci`\n"

		embed = discord.Embed(title = f'Portions Commands', url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fd39vzol73omnio.cloudfront.net%2Fwp-content%2Fuploads%2F2015%2F07%2FSh5OUBgauqHJL300-500x4001.jpg&f=1&nofb=1', 
				description = description, color = 0xCF0A0E)
		await message.channel.send(embed = embed)






		
			
		
					
		
client.run(token)  
