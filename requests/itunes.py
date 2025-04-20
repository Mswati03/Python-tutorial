import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?term=" + sys.argv[1] + "&limit=1")

print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:
    print(result["trackName"])
#json.dumps for pretty printing for easy reading of json output