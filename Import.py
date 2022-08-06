import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"id":"276","season":"2020"}

headers = {
	"X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)