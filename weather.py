#%%

import requests
import json

def get_url():
    lat = 23.55
    lon = -46.64
    url = "https://api.open-meteo.com/v1/forecast?latitude="
    url += str(lat) + "&longitude="
    url += str(lon)
    url += "&current_weather=true&hourly=temperature_2m"
    # url += "&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    #
    return url
#

def get_weather_dic(url):
    headers = {"accept": "application/json"}
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    dic = json.loads(response.text)
    return dic
#

url = get_url()
dic = get_weather_dic(url)

# %%
dic["current_weather"]["temperature"]

# %%
list_time = dic["hourly"]["time"]
list_temperature = dic["hourly"]["temperature_2m"]


# %%
import altair as alt
import pandas as pd
df = pd.DataFrame(
    list(zip(pd.to_datetime(list_time), list_temperature)),
    columns=["time", "temperature"]
)

#%%

alt.Chart(df).mark_circle().encode(
    x = "time",
    y = "temperature"
)
# %%
