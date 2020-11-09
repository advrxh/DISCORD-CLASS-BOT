import discord
from random import choice

from user_defined import TOKEN_1, TOKEN_2
from get_period import period

token = str(TOKEN_1 + TOKEN_2)
client = discord.Client()  


@client.event  
async def on_ready(): 
    print(f'We have logged in as {client.user}') 

aadil_commands = ['Hey master... ur the only person i care of :heart_eyes: ', 'Ohh my beloved boss :heart:', 'Hey can i tell u something u are cute!']
tharun_commands = ['Hey dude u suck at codm!! :smirk:', 'hey dont worry Petty wont dissapoint u ! :rofl: :rofl: :rofl:', 'Hey how is Ms.Prathiba? :rofl:', 'You are the biggest simp i have ever seen in my bot carrier! :hugging: :hugging_face:']
lakshmi_commands = ['Hey mind if i say something BTS SUCKS it really sucks.. :smirk: :rofl:', 'Hey how do u even recognize those guys at BTS..:rofl: :rofl: :rofl:', 'btw u really didnt suit for the narrators role :smirk: ', 'Lakshmi u are not the good girl i am :smirk:']
suzanne_commands = ['Hey hows balendran doing :rofl:' , 'u really dont have a humour sense :rofl:', '999 rs is a bit low for a book from an author like u :joy::rofl:']

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
