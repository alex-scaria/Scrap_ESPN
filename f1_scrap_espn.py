from lxml import html
import requests
import pandas as pd


page = requests.get('https://www.espn.in/f1/story/_/id/18842142/2019-formula-1-season-drivers')
tree = html.fromstring(page.content)


drivers_tree = tree.xpath('//table')

#drivers=[]
#for driver in drivers_tree:
#    driver = driver.text_content()
#    drivers.append(driver)



col=[]
i=0
for heading in drivers_tree[0][0]:
    for k in heading:
            i+= 1
            name = k.text_content()
            print('%d:"%s"'%(i,name))
            col.append((name,[]))
    
for j in range(0,len(drivers_tree[0][1])):
    T=drivers_tree[0][1][j]
    if len(T)!=3:
        break
    i=0
    for d in T.iterchildren():
        data=d.text_content().strip() 
        col[i][1].append(data)
        i+=1
        
Dict_f1 = {title:column for (title,column) in col}
