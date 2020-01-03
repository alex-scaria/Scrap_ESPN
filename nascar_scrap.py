from lxml import html
import requests
import pandas as pd


page_nascar = requests.get('http://www.espn.com/racing/drivers')
tree_nascar = html.fromstring(page_nascar.content)


d = tree_nascar.cssselect('td')

drivers = []
for driver in d:
    driver = driver.text_content()
    drivers.append(driver)

del drivers[0]

i=0
new_list=[]
while i<len(drivers):
  new_list.append(drivers[i:i+5])
  i+=5

df_nascar = pd.DataFrame(new_list[1:], columns = new_list[0])
