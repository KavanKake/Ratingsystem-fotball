import json
import requests


url = 'https://www.fotmob.com/api/matchDetails'
response = requests.get(url, params={
    'matchId': 4506859})
if response.status_code == 200:
    posts = response.json()
else:
    print('Error:', response.status_code)





# starters = posts["content"]["lineup"]["awayTeam"]["starters"]

# subs = posts["content"]["lineup"]["awayTeam"]["subs"]

# unavailable = posts["content"]["lineup"]["awayTeam"]["unavailable"]

# players = starters + subs + unavailable

