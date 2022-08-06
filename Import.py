import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"id":"276","season":"2020"}

headers = {
	"X-RapidAPI-Key": 
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
