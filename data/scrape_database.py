#!/usr/bin/env python3
import pandas as pd
from bs4 import BeautifulSoup

# Read saved webpage into beautifulsoup
with open('index.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html')

# Page is split so each station is 'tr', and each
# feature for a station is labelled 'td'

elements = soup.find_all('tr')
column_names = []
# Grab the names of the columns
for i in elements[2].find_all('td'):
    column_names.append(i.text)

# Last column in data isn't labelled
column_names[-1] = 'P. Unit'

# Grab the foe each station and split it up into its features
content_list = []
for i in range(3,len(elements)):
    content_list.append([a.text for a in elements[i].find_all('td')])

# Output to file
df = pd.DataFrame(content_list[:-9],columns = column_names)
df.to_csv('radio_list.csv',index=False)
