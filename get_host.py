from googlesearch import search
results = []
query = 'what is my ip?'

for i in search(query, num_results=3):
  results.append(i)
  print(i)
