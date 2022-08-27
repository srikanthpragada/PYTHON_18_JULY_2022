
import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details")
    exit()

countries = resp.json()  # convert json[] to list[dict]

for c in countries:
    name = c['name']['common']
    region = c['region']
    population =c['population']
    print(f"{name:50} {region:15}  {population:10}")



