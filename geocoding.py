## GCP
# https://developers.google.com/maps/documentation/geocoding/start
# https://developers.google.com/maps/documentation/geocoding/requests-reverse-geocoding

import requests
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_MAPS_API")

### create loop, exampple list of data address to go through 
### and hit the API 
def geocode(address_here): 
    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address_here
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address_here, 'lat': lat_response, 'lon': lng_response}
    return final 


# go through list of 100 random adddresses and geocode them
def geocode_100_address():
    df = pd.read_csv('addresses.csv')
    for address in df.values: 
        print(geocode(' '.join(address)))

geocode_100_address()


## Reverse Geocode 
def reverse_geocode(lat,lng): 
    search = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='


    url_request_part1 = search + lat + ',' + lng + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()
    for address in response_dictionary['results']:
        print({'lat': lat, 'lon': lng, 'address': address['formatted_address']})

def reverse_geocode_100_lat_lng():
    df = pd.read_csv('lat_lng.csv')
    for item in df.values:
        input_lat = str(item[0])
        input_lng = str(item[1])
        print(reverse_geocode(input_lat,input_lng))

reverse_geocode_100_lat_lng()

