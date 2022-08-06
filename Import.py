import requests
import USERINPUT

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"league": "61", "season": "2021", "search": "neymar"}

headers = {
	"X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
