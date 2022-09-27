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

with open("wikipedia_python_2.html", 'w') as open_file:
    file_open.write(data)

