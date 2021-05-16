import requests
import json

COUNTRY_CODE = input("Enter Country Code: ")
POSTCODE = int(input("Enter pincode: "))

response = requests.get(f"https://api.zippopotam.us/{COUNTRY_CODE}/{POSTCODE}")
json_response = response.json()

try:
	print(f'Country: {json_response["country"]}')
	print(f'Place Name: {json_response["places"][0]["place name"]}')
	print(f'State: {json_response["places"][0]["state"]}')

except:
	print("Invalid Request")





