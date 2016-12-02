import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime
 
# TODO: Ask for place of farm to get weather


# Source: https://developer.ibm.com/clouddataservices/2016/10/06/your-own-weather-forecast-in-a-python-notebook/ 

# Weather company data API credentials
username='13a81639-0c93-45bb-95e9-4ba7e1cb5cb8'
password='GMUfrv696Z'
 
# Request forecast for London
lat = '51.49999473'
lon = '-0.116721844'
line='https://'+username+':'+password+'@twcservice.mybluemix.net/api/weather/v1/geocode/'+lat+'/'+lon+'/forecast/intraday/10day.json?&units=m'
r=requests.get(line)
weather = json.loads(r.text)    
 
#print json.dumps(weather,indent=1)
 
df = pd.DataFrame.from_dict(weather['forecasts'][0],orient='index').transpose()
for forecast in weather['forecasts'][1:]:
    df = pd.concat([df, pd.DataFrame.from_dict(forecast,orient='index').transpose()])
 
# extract time and use it as index
time = np.array(df['fcst_valid_local'])
for row in range(len(time)):
    time[row] = datetime.strptime(time[row], '%Y-%m-%dT%H:%M:%S+0000') #0010
 
df = df.set_index(time)
     
list(df)

df.to_pickle('/home/juwinkler/hackathon/cognitivefarming/pandaWeather.p')
df.to_csv('/home/juwinkler/hackathon/cognitivefarming/pandaWeather.csv')
print(df)
