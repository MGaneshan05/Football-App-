import requests
import json
import re


def team(club, leg):

	url = "https://api-football-v1.p.rapidapi.com/v3/teams"

	querystring = {"name": "%s" % club, "league": "%s" % leg, "season": "2020"}

	headers = {
		"X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	r = response.json()

	json_object = json.dumps(r, indent=4)

	# Writing to sample.json
	with open("user_team.json", "w") as outfile:
		outfile.write(json_object)

	# Reading from json file
	with open('user_team.json', 'r') as openfile:
		json_object = json.load(openfile)

	s = str(json_object['response'][0])

	k = str(re.search(r'\d+', s).group())
	# print(s[18:20])
	lig = s[18:20]
	return k
