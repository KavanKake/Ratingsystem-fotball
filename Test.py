import json

# Step 1: Load the JSON file
file_path = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Laliga.json"

match_stats = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/BarcelonaVSRealValledolid.json"

# Open the file and load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)  # Load the JSON content into a Python dictionary

with open(match_stats,"r") as file:
    stats = json.load(file)

# Step 2: Access the 'Barcelona' data
barcelona_data = data["La liga"]["Barcelona"]
teams_stats = stats["content"]["playerStats"]


# Step 4: Access specific parts (like Players)
barcelona_players = barcelona_data["Players"]


# Print all players from Barcelona
for player_id, player_info in barcelona_players.items():
    print(f"Player ID: {player_id}, Name: {player_info['name']}")


    







