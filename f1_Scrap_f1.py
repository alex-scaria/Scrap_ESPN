from lxml import html
import requests
import pandas as pd


page_f1 = requests.get('https://www.formula1.com/en/drivers.html')
tree_f1 = html.fromstring(page_f1.content)
    
    
b = tree_f1.cssselect(".driver-name")
names=[]
for name in b:
    name = name.text_content()
    names.append(name)
    
c = tree_f1.cssselect(".driver-team")
teams=[]
for team in c:
    team = team.text_content()
    teams.append(team)

#teams = [team.replace("\n","") for team in teams]
#
#for team in teams:
#    team.replace(" ", "")

details = list(zip(names, teams))

df = pd.DataFrame(details, columns = ['Name', 'Team'])
