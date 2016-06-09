import requests
import os
key = os.environ['met_key']
url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3544?res=hourly&key='

response = requests.get(url+key)
   
data = response.json()

print data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['T']
