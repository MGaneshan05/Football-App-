import requests
import json
import re


def league(country, lge, szn):

	url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

	querystring = {"name": "%s" % lge, "country": "%s" % country, "season": "%s" % szn}

	headers = {"X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315" ,
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
	return m

