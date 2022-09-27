# %%

import requests 

url = 'https://pt.wikipedia.org/wiki/Python'
data = requests.get(url).text

print(data)
# %%

file_open = open("wikipedia_python.html", 'w')
file_open.write(data)
file_open.close()
# %%
