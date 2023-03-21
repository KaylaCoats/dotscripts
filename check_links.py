#!/usr/bin/env python3
import requests
import os
from bs4 import BeautifulSoup
from sys import argv

#Take url from argv and run requests
resp  = requests.get(argv[1])

#Get html from url
soup = BeautifulSoup(resp.text, features='html.parser')

#Find all the links in a tags
links = soup.find_all('a')

#Put links and text into dictionary
n_links = {}
for link in links:
    link = str(link)
    link = link.split('"')
    url = link[1]
    tag = link[2][1:len(link[2])-len('</a>')]
    n_links.update({url:tag})
    
#Find and create file of bad links text
bad_links = []

for link in n_links.keys():
    n_link = argv[1]+link
    indv_resp = requests.get(n_link)
    if indv_resp.status_code == 404:
        bad_links.append(n_links[link])

if os.path.exists('../.links/bad-links.txt'):
    os.remove('../.links/bad-links.txt')

with open('../.links/bad-links.txt', 'w') as f:
    bad_links = '\n'.join(bad_links)
    f.write(bad_links)

