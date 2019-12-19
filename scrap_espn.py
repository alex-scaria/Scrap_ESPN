import pandas as pd
import requests
import json
import datetime



    


def data(page):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.espn.in',
        'Connection': 'keep-alive',
        'Referer': 'https://www.espn.in/football/transfers',
        'TE': 'Trailers',
    }
    
    params = (
        ('region', 'in'),
        ('lang', 'en'),
        ('contentorigin', 'espn'),
        ('sort', 'date:desc,fee:desc'),
        ('limit', '3'),
        ('page', page),
    )
    
    response = requests.get('https://site.web.api.espn.com/apis/site/v2/sports/soccer/all/transactions'
                            , headers=headers, params=params)
    
    data = json.loads(response.text)
    #df = pd.DataFrame(list(data['transactions']))
    return data


transfer = []
for i in range(1, 480):
    tran=data(i)['transactions']
    transfer.append(tran)    
  
       
name=[]
date=[]
from_team=[]
to_team=[]
amount=[]
display_amount=[]
typeof=[]
links=[]
seasons=[]
player_id=[]

for i in range(0,479):
    for j in range(0,3):
        print(i,j)
        try:
            p_id=transfer[i][j]['athlete']['id']
            player_id.append(p_id)
        except:
            player_id.append("NULL")
        nam=transfer[i][j]['athlete']['displayName']
        name.append(nam)
        
        dat=transfer[i][j]['date']
        dat = datetime.datetime.strptime(dat, "%Y-%m-%dT%M:%SZ")
        date.append(dat)
        
        fr_team=transfer[i][j]['from']['displayName']
        from_team.append(fr_team)
        t_team=transfer[i][j]['to']['displayName']
        to_team.append(t_team)
        amt=transfer[i][j]['amount']
        amount.append(amt)
        dp_amount=transfer[i][j]['displayAmount']
        display_amount.append(dp_amount)
        ty_of=transfer[i][j]['type']
        typeof.append(ty_of)
        try:
            link=transfer[i][j]['links']['href']
            links.append(link)
        except:
            links.append('NULL')
    
final_df = pd.DataFrame(list(zip(player_id, date, name, from_team, to_team, amount, display_amount, typeof, links)), columns = ['ID', 'Date', 'Player Name', 'From', 'To', 'Amount', 'Display Amount', 'Type', 'Link']) 
out_json = final_df.to_json(orient='records')[1:-1].replace('},{', '} {')
transfer_dict = final_df.T.to_dict().values()
