import json

# Load player data for Barcelona from the API
file_path = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Laliga.json"
with open(file_path, 'r') as file:
    player_data = json.load(file)  # Load the JSON content into a Python dictionary
barcelona_club = player_data["La liga"]["Barcelona"]
team_id = barcelona_club["id"]
barcelona_players = barcelona_club["Players"]


# Hometeam or awayteam and unavailable players
unavailable_player_ids_list = []

# Load match data
match_BarcelonaVSRealValledolid = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/BarcelonaVSRealValledolid.json"
with open(match_BarcelonaVSRealValledolid, "r") as file:
    lineup = json.load(file)

# Check if Barcelona is the home team
hometeam_id = lineup["content"]["lineup"]["homeTeam"]["id"]

if hometeam_id == team_id: 
    unavailable_player_ids = lineup["content"]["lineup"]["homeTeam"]["unavailable"]
else:
    unavailable_player_ids = lineup["content"]["lineup"]["awayTeam"]["unavailable"]

# Add unavailable player IDs to list
for player in unavailable_player_ids:
    unavailable_player_ids_list.append(player["id"])

# Iterate over Barcelona players and print stats for available players
for player_id, player_info in barcelona_players.items():
    # Skip players if they are in the unavailable list
    if player_id in unavailable_player_ids_list:
        continue  # Skip this player
    
    # Load match stats
    with open(match_BarcelonaVSRealValledolid, "r") as file:
        stats = json.load(file)
    
    team_stats = stats["content"]["playerStats"]

    # Check if player stats are available
    if player_id in team_stats:
        player_allstats = team_stats[player_id]
        player_mystats = player_allstats["stats"]
        
        # Print player stats
        print(f"Player ID: {player_id}, Name: {player_info['name']}")
        print(player_mystats)
        print("")
    else:
        print(f"No stats available for Player ID: {player_id}, Name: {player_info['name']}")
        print("")
