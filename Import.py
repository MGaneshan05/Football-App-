import requests
import USERINPUT

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"league": "61", "season": "2021", "search": "neymar"}

headers = {
	"X-RapidAPI-Key": 
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
