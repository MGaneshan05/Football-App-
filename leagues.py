import requests
import json
import re


def league(country, lge):

	url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

	querystring = {"name": "%s" % lge, "country": "%s" % country, "season": "2020"}

	headers = {"X-RapidAPI-Key":  ,
				"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	r = response.json()

	json_object = json.dumps(r, indent=4)

	# Writing to sample.json
	with open("user_league.json", "w") as outfile:
		outfile.write(json_object)

	# Reading from json file
	with open('user_league.json', 'r') as openfile:
		json_object = json.load(openfile)

	s = str(json_object['response'][0])

	m = str(re.search(r'\d+', s).group())
	# print(s[18:20])
	lig = s[18:20]
	return m

