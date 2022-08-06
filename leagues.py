
import requests
import json
url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

querystring = {"name":"premier league","country":"england","season":"2020"}

headers = {
	"X-RapidAPI-Key":  ,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

r = response.json()

json_object = json.dumps(r, indent=4)

# Writing to sample.json
with open("user_league.json", "w") as outfile:
	outfile.write(json_object)

with open('user_league.json', 'r') as openfile:
	# Reading from json file
	json_object = json.load(openfile)

s = str(json_object['response'][0])
print(s[18:20])
lig = s[18:20]

