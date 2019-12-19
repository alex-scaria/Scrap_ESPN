

from lxml import html
import requests
import pandas as pd


page = requests.get('https://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors')
tree = html.fromstring(page.content)


players = tree.xpath('//span//a[@class = "AnchorLink"]/text()')
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
df = pd.DataFrame(Dict)
nba_dict = df.T.to_dict().values()
