import json
from random import choice

with open('quotes.json', 'r', encoding = 'cp1252') as f:
	data = json.load(f)

rand_no = list(range(0, 5421))

def quote(list_, data):
	cur_choice = choice(list_)
	return (data[cur_choice]['quoteText'], data[cur_choice]['quoteAuthor'])


print(quote(rand_no, data))
















