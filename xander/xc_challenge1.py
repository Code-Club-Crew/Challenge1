#!/usr/local/bin/python

import requests
import json

for i in range(1, 999999):
    try:
        r = "https://swapi.co/api/starships/?page=%s" % i
        response = requests.request("GET", r)
        j = json.loads(response.text)

        theResults = j['results']
        for i in range(len(theResults)):
            jasontemp = theResults[i]
            starshiplist = jasontemp['name']
            pilotlist = jasontemp['pilots']
            if pilotlist:
                print(starshiplist)
                i = 0
                while i < len(pilotlist):
                    eachPilot = requests.get(pilotlist[i])
                    individualPilotJson = json.loads(eachPilot.text)
                    print("  ", individualPilotJson['name'])
                    i += 1
    except KeyError:
        break