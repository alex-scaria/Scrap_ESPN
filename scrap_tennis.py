from lxml import html
import requests
import pandas as pd


page_tennis = requests.get('http://www.espn.com/tennis/players')
tree_tennis = html.fromstring(page_tennis.content)
    
    
p = tree_tennis.cssselect(".tablehead a")

players = []
for player in p:
    player = player.text_content()
    players.append(player)

c = tree_tennis.cssselect("td + td")

countries = []
for country in  c:
        country = country.text_content()
        if len(country) == 0:
            countries.append("Null")
        else:
            countries.append(country)

for alll in countries:
    if "COUNTRY" in countries: countries.remove("COUNTRY")

df_tennis = pd.DataFrame(list(zip(players, countries)), columns = ['Name', 'Country'])


page_ranking = requests.get("https://www.espn.com/tennis/rankings")
tree_ranking = html.fromstring(page_ranking.content)

r = tree_ranking.cssselect(".Table__TD , .mr7")

rankings = []
for i in r:
    i = i.text_content()
    rankings.append(i)

#table_tree = tree_tennis.xpath('//td')
#z=[]
#for t in table_tree:
#    t = t.text_content()
#    z.append(t)             
#
#col=[table_tree[1].text_content(), table_tree[2].text_content()]
#
#players=[]
#for t in table_tree:
#    player = t.text_content()#[3:len(table_tree):2]
#    players.append(player)
# 
#players = players[3:len(table_tree):2]
#for player in players:
#    player = 
#
#
#i=0
#for t in table_tree[1]:
#    i+= 1
#    name = t.text_content()
#    #print(name)
#    print('%d:"%s"'%(i,name))
#    col.append((name,[]))
#    
#for j in range(1,len(table_tree)):
#    T=table_tree[j]
#    if len(T)!=2:
#        break
#    i=0
#    for t in T.iterchildren():
#        data=t.text_content().strip() 
#        col[i][1].append(data)
#        i+=1
#        
#Dict_tennis = {title:column for (title,column) in col}

