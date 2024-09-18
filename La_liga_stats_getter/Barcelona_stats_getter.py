import json

# Load player data for Barcelona from the API
file_path = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/League_apis/Laliga.json"
with open(file_path, 'r') as file:
    player_data = json.load(file)  # Load the JSON content into a Python dictionary
barcelona_club = player_data["La liga"]["Barcelona"]
team_id = barcelona_club["id"]
barcelona_players = barcelona_club["Players"]


# Hometeam or awayteam and unavailable players
unavailable_id_list = []

# Load match data
print("1. Valencia Vs FC Barcelona")
print("2. FC Barcelona VS Athletic Club")
print("3. Rayo Vallecano Vs FC Barcelona")
print("4. FC Barcelona Vs Real Valledolid")
print("5. Girona Vs FC Barcelona")

which_match = int(input("Choice one of the matches above!"))

if which_match == 2: 
    match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/BarcelonaVSAthleticClub.json"
elif which_match == 4: 
    match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/BarcelonaVSRealValledolid.json"
elif which_match == 5: 
    match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/GironaVSBarcelona.json"
elif which_match == 3: 
    match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/RayoVallecanoVSBarcelona.json"
elif which_match == 1: 
    match_file= "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/ValenciaVSBarcelona.json"
else: 
    print("invalid answar, please choise a number from 1-5!")

with open(match_file, "r") as file:
    lineup = json.load(file)

# Check if Barcelona is the home team
hometeam_id = lineup["content"]["lineup"]["homeTeam"]["id"]

if hometeam_id == team_id: 
    unavailable = lineup["content"]["lineup"]["homeTeam"]["unavailable"]
else:
    unavailable = lineup["content"]["lineup"]["awayTeam"]["unavailable"]

# Add unavailable player IDs to list
for player in unavailable:
    unavailable_id_list.append(player["id"])




# Iterate over Barcelona players and print stats for available players
for player_id, player_info in barcelona_players.items():
    # Skip players if they are in the unavailable list
    if player_id in unavailable_id_list:
        continue  # Skip this player
    
    # Load match stats
    with open(match_file, "r") as file:
        stats = json.load(file)
    
    team_stats = stats["content"]["playerStats"]

    # Check if player stats are available
    if player_id in team_stats:
        player_allstats = team_stats[player_id]
        player_mystats = player_allstats["stats"]
        if player_mystats == []:
            print(f"Player ID: {player_id}, Name: {player_info['name']}, was benched")
            print("")
        else: 
            # Print player stats
            print(f"Player ID: {player_id}, Name: {player_info['name']}")
            print(player_mystats)
            print("")
    else:
        print(f"No stats available for Player ID: {player_id}, Name: {player_info['name']}")
        print("")
