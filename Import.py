import requests
import USERINPUT
import leagues
import teams


url = "https://api-football-v1.p.rapidapi.com/v3/players"

inputs = USERINPUT.user_input()
lg = leagues.league(inputs[0], inputs[1])
print(lg)
team = teams.team(inputs[4], lg)
print(team)
querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % inputs[2], "search": "%s" % inputs[3]}

headers = {
	"X-RapidAPI-Key": ,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())