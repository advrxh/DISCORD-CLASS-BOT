import json
from random import choice

with open('quotes.json', 'r+', encoding = 'utf-8') as f:
	data = json.load(f)

rand_no = list(range(0, 101))

def quote(list_, data):
	cur_choice = choice(list_)
	return (data['quotes'][cur_choice]['quote'], data['quotes'][cur_choice]['author'])

















