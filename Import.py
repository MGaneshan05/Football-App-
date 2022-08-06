import requests
import USERINPUT

url = "https://api-football-v1.p.rapidapi.com/v3/players"

inputs = USERINPUT.user_input()

querystring = {"league": "%s" % inputs[0],"season": "%s" % inputs[1], "search": "%s" % inputs[2]}

headers = {
	"X-RapidAPI-Key": ,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())