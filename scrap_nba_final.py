
from lxml import html
import requests
import pandas as pd
import re

start_url = 'http://www.espn.com/nba/players'
response = requests.get(start_url)
tree_url = html.fromstring(response.text)
links = tree_url.cssselect('.small-logos div a')



out = []
for link in links:
    if 'href' in link.attrib:
        out.append(link.attrib['href'])
        
team_names = [] 
for i in out:
        name = i[-3:]
        team_names.append(name)
#        if name:
#            found = name.group(1)
#            team_names.append(found)

string = 'http://www.espn.com'
urls = [string + x for x in out]

pages = []
trees = []
for url in urls:
    page = requests.get(url)
    pages.append(page)
 
for page in pages:
    tree = html.fromstring(page.content)
    trees.append(tree)


for (nam, tree) in zip(team_names, trees):
    tr_elements = tree.xpath('//tr')
    col=[]
    i=0
    for t in tr_elements[0]:
        i+= 1
        name = t.text_content()
        print('%d:"%s"'%(i,name))
        col.append((name,[]))
        
    for j in range(1,len(tr_elements)):
        T=tr_elements[j]
        if len(T)!=8:
            break
        i=0
        for t in T.iterchildren():
            data=t.text_content().strip() 
            col[i][1].append(data)
            i+=1
     
    Dict = {title:column for (title,column) in col}
    nam = pd.DataFrame(Dict)
    nam.to_csv(nam.csv)
        
        