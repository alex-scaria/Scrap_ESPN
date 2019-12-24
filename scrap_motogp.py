from lxml import html
import requests
import pandas as pd


page_motourl = requests.get('https://www.motogp.com/en/riders/MotoGP')
tree_motourl = html.fromstring(page_motourl.content)
    

links = tree_motourl.cssselect(".name a")



moto_urls = []
for link in links:
    if 'href' in link.attrib:
        moto_urls.append(link.attrib['href'])


names = []
teams = []
bikes = []
places = []
dobs = []
weights = []
heights = []



for url in moto_urls:
    print(url)
    page_motogp = requests.get(url)
    tree_motogp = html.fromstring(page_motogp.content)
    
    

    
    n = tree_motogp.cssselect(".name")
    t = tree_motogp.cssselect(".team")
    b = tree_motogp.cssselect(".team+ p")
    p = tree_motogp.cssselect("p:nth-child(6)")
    d = tree_motogp.cssselect("p:nth-child(7)")
    w = tree_motogp.cssselect("p:nth-child(8)")
    h = tree_motogp.cssselect("p:nth-child(9)")
    

    for name in n:
        name = name.text_content()
        names.append(name)
    
    for team in t:
        team = team.text_content()
        teams.append(team)
        
    for bike in b:
        bike = bike.text_content()
        bikes.append(bike)
        
    for place in p:
        place = place.text_content()
        places.append(place)
        
    for dob in d:
        dob = dob.text_content()
        dobs.append(dob)
        
    for weight in w:
        weight = weight.text_content()
        weights.append(weight)
        
    for height in h:
        height = height.text_content()
        heights.append(height)
    
    
    
    


