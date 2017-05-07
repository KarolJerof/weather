import datapoint
import pprint
import numpy as np
import pandas as pd
import geocoder

# Get longitude and latitude from postcode
g = geocoder.google('NW32EH')
g.latlng

conn = datapoint.connection(api_key="819006d9-96a8-46e5-83db-a28c702e61d8")
all_sites = conn.get_all_sites()
site = conn.get_nearest_site(g.lng, g.lat) # longitude and latitude
forecast = conn.get_forecast_for_site(site.id, "3hourly")

# Print current weather
current_timestep = forecast.now()
pprint.pprint(str(current_timestep.date))
pprint.pprint(current_timestep.weather.text)
pprint.pprint(str(current_timestep.temperature.value) + current_timestep.temperature.units) # tempreture

# This example will print out a simple forecast for the next 5 days
# Loop through days
date = []
time = []
weather = []
temperature = []
humidity = []
precipitation = []
uv = []
visibility = []
wind_direction = []
wind_gust = []
wind_speed = []

for day in forecast.days:
    #pprint.pprint(str(day.date))
    for t in day.timesteps:
        pprint.pprint(str(t.date))
        date.append(t.date.date())
        time.append(t.date.time())
        weather.append(t.weather.text)
        temperature.append(t.temperature.value)
        humidity.append(t.humidity.value)
        precipitation.append(t.precipitation.value)
        uv.append(t.uv.value)
        visibility.append(t.visibility.value)
        wind_direction.append(t.wind_direction.value)
        wind_gust.append(t.wind_gust.value)
        wind_speed.append(t.wind_speed.value)

df = pd.DataFrame([date, time, weather, wind_direction, temperature,humidity, precipitation,uv,
                   visibility, wind_speed, wind_gust]).T

df.columns = ['date', 'time', 'weather', 'wind_direction', 'temperature','humidity', 'precipitation','uv',
                   'visibility', 'wind_speed', 'wind_gust']