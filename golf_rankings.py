from lxml import html
import requests
import pandas as pd

#############RANKINGS####################################
page_golf = requests.get('https://www.espn.in/golf/rankings')
tree_golf = html.fromstring(page_golf.content)


p = tree_golf.cssselect('.Table__TD')


rkings = []
for ranking in p[:400]:
    ranking = ranking.text_content()
    rkings.append(ranking)
    
    
i=0
rankings=[]
while i<len(rkings):
  rankings.append(rkings[i:i+2])
  i+=2
    
#rankings = rkings[::2]
#names = rkings[1::2] 

points = []
for point in p[400:]:
    point = point.text_content()
    points.append(point)
 
i=0
pts=[]
while i<len(points):
  pts.append(points[i:i+5])
  i+=5
  
def merge(rankings, pts): 
    return [(sub + [pts[i][0]] + [pts[i][1]] + [pts[i][2]] + [pts[i][3]] + [pts[i][4]] ) for i, sub in enumerate(rankings)]
new = merge(rankings, pts)


  
golf_rankings = pd.DataFrame(new, columns = ['Ranking', 'Name', 'AVG points', 'Total points', 'Events', 'PTS Lost', 'PTS Gain'])


##########################PLAYERS#################################


page_golf_players = requests.get('http://www.espn.com/golf/players')
tree_golf_players = html.fromstring(page_golf_players.content)


n = tree_golf_players.cssselect('#my-players-table a')

names = []

for name in n :
    name = name.text_content()
    names.append(name)
    
c = tree_golf_players.cssselect('td+ td')

countries = []

for country in c:
    country = country.text_content()
    countries.append(country)

for alll in countries:
    if "COUNTRY" in countries: countries.remove("COUNTRY")
    
golf_players = pd.DataFrame(list(zip(names, countries)), columns = ['Name', 'Country'])
