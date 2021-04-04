#!/usr/bin/python
import json
import requests
import pandas as pd
import datetime as dt

token= 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBiNWFiMjJjMTlmNzNhYWFlZmEyYzU5NGEyYTdiNzAxZDU4ZjQzYjVkNDgwOWYxZmJkY2E2YzBhOTc3NGQxMTM5ZDc2YmUxNzA0YTE1YzNjIn0.eyJhdWQiOiIyIiwianRpIjoiMGI1YWIyMmMxOWY3M2FhYWVmYTJjNTk0YTJhN2I3MDFkNThmNDNiNWQ0ODA5ZjFmYmRjYTZjMGE5Nzc0ZDExMzlkNzZiZTE3MDRhMTVjM2MiLCJpYXQiOjE2MTc1NDMyMDYsIm5iZiI6MTYxNzU0MzIwNiwiZXhwIjoxNjQ5MDc5MjA2LCJzdWIiOiIxMzYwIiwic2NvcGVzIjpbXX0.A_sbVQ_4f-3tWeNtGK7K9HP_fL0G5LexUUznZpsn8svRGAG-trasoIMw5iVSRRXw0ktfSgAk7SvlGr8U5_6CUvBaBs2MrPAaazSG-myB8H_6_XP8VPWSrEP-xY7MokqYR6C5lJgXY9LFur7cVs0_2w-7cG-IsSOL6faspPFjXrTAGTWm8w9z7AdHFWOhNXPQu5bnLIyxhJUejIw-A9750cCOEv5Az415VGBht3T1qtPRs9762qaKXqFM3Yc5RbF7akqTL8P8Du3jbUK17N6Dlw7jo7WOTXRxTC4WdtTXamOJLJOuYVhAxvpnWoLL43Q8n7TY8mZL3rJbQc3eg2F-ApOPp5T1dCh5M0mkQwKrGrFR4MLN8RFc_h4SlvhwRJ1d8_rGrz1YwF-JikeueGWcGBJErGhgiB2FWTV_lUUJ6B2WQVsaYJ5A6qoOMWmwG0miWCOZIqeJK_xdyATB86hvCASrIpr_ImPNh0gJbzkN3wmxKcNOHIrmempC5UAlHP3qUwa_pQpODA1OrGPkvkxPbcn8tjzaPhh5lOGp2NM6HiIvDRdrUNJgDrcOBN7qp3OsL4HnoPbGZl9SxqPGqccQ9iEP4zGapJdE2fzSxHh0ws3cihEe5cPKLEu8BgAe9vkMX47ZbMHO8P7gA1tlWm_LrmfHG-Sb642UrGNXaP0p0U8'

# Province
lat =  9.401
long = 98.392

t = dt.datetime.now()+dt.timedelta(hours=1)

url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/at"

querystring = {
    "lat":"%s"%lat,
    "lon":"%s"%long,
    "fields":"tc,rh,rain",
    "date":"%s-%02d-%02d"%(t.year,t.month,t.day),
    "hour":"%s"%(t.hour),
    "duration":"1"
   }
headers = {
   'accept': "application/json",
   'authorization': "Bearer "+token,
    }

response = requests.request("GET", url, headers=headers, params=querystring)
d=json.loads(response.text)
d =  {
        'lat': d['WeatherForecasts'][0]['location']['lat'],
        'lon': d['WeatherForecasts'][0]['location']['lon'],
        'time': d['WeatherForecasts'][0]['forecasts'][0]['time'],
        'rh': d['WeatherForecasts'][0]['forecasts'][0]['data']['rh'],
        'tc': d['WeatherForecasts'][0]['forecasts'][0]['data']['tc'],
        'rain': d['WeatherForecasts'][0]['forecasts'][0]['data']['rain']
    }
df_out = pd.read_csv('/home/chayapone001/Chayapone_TMD_Contab/TMD_data_Jay.csv')
df_out = df_out.drop(columns=['Unnamed: 0'])
df_out.loc[len(df_out)]=['Ranong',d['time'],d['tc'],d['rh'],d['rain']]
df_out.to_csv('/home/chayapone001/Chayapone_TMD_Contab/TMD_data_Jay.csv')
