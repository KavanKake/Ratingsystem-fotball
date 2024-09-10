import json

# Load data from the external JSON file
def load_player_stats_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Example of loading external data
external_data_file = 'BarcelonaVSRealValledolid.json'
external_player_stats = load_player_stats_from_file(external_data_file)

# Player data from the API
file_path = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Laliga.json"
with open(file_path, 'r') as file:
    data = json.load(file)  # Load the JSON content into a Python dictionary

barcelona_club = data["La liga"]["Barcelona"]
barcelona_players = barcelona_club["Players"]
for player_id, player_info in barcelona_players.items():
    print(f"Player ID: {player_id}, Name: {player_info['name']}")

print("   ")

# TODO fiks løkke for skadede spillere. 

for player_id, player_info in barcelona_players.items():
    match_stats = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/BarcelonaVSRealValledolid.json"
    with open(match_stats,"r") as file:
        stats = json.load(file)

    player_variabel_id = player_id
    team_stats = stats["content"]["playerStats"]
    player = team_stats[player_variabel_id]
    print(player)
    print ("  ")




# Poengberegning
def calculate_points(stats):
    points = 0

    # Goals and assists
    goals = stats['stats'][0]['stats']['Goals']['value']
    assists = stats['stats'][0]['stats']['Assists']['value']
    if goals >= 3:
        points += 3
    else:
        points += goals * 1.5

    if assists >= 3:
        points += 3
    else:
        points += assists * 1.5

    # Passning presisjon    
    accurate_passes = stats['stats'][0]['stats']['Accurate passes']['value']
    total_passes = stats['stats'][0]['stats']['Accurate passes']['total']
    pass_accuracy = (accurate_passes / total_passes) * 100
    if pass_accuracy == 10:
        points += 0.1
    elif pass_accuracy <= 20:
        points += 0.2
    elif pass_accuracy <= 30:
        points += 0.3
    elif pass_accuracy <= 40:
        points += 0.4
    elif pass_accuracy <= 50:
        points += 0.5
    elif pass_accuracy <= 60:
        points += 0.6
    elif pass_accuracy <= 70:
        points += 0.7
    elif pass_accuracy <= 80:
        points += 0.8
    elif pass_accuracy <= 90:
        points += 0.9
    else:
        points += 1.0

    # Fratatt ballen
    dispossessed = stats['stats'][1]['stats']['Dispossessed']['value']
    if dispossessed == 0 or dispossessed == 1:
        points += 0
    elif dispossessed <= 3:
        points -= 0.1
    elif dispossessed <= 4:
        points -= 0.2
    else:
        points -= 0.3

    # Vellykkede taklinger
    tackles_won = stats['stats'][2]['stats']['Tackles won']['value']
    if tackles_won <= 20:
        points += 0.1
    elif tackles_won <= 40:
        points += 0.2
    elif tackles_won <= 60:
        points += 0.3
    elif tackles_won <= 80:
        points += 0.4
    else:
        points += 0.5

    # Vellykkede driblinger
    successful_dribbles = stats['stats'][1]['stats']['Successful dribbles']['value']
    total_dribbles = stats['stats'][1]['stats']['Successful dribbles']['total']
    dribble_accuracy = (successful_dribbles / total_dribbles) * 100
    if dribble_accuracy <= 20:
        points += 0.1
    elif dribble_accuracy <= 40:
        points += 0.2
    elif dribble_accuracy <= 60:
        points += 0.3
    elif dribble_accuracy <= 80:
        points += 0.4
    else:
        points += 0.5

    # Disiplin
    yellow_cards = stats['stats'][3]['stats']['Fouls committed']['value']  # Assume yellow cards
    red_cards = stats['stats'][3]['stats']['Fouls committed']['value']  # Assume red cards
    points -= yellow_cards * 0.5
    points -= red_cards * 1.0

    # Spilt 60 min
    minutes_played = stats['stats'][0]['stats']['Minutes played']['value']
    if minutes_played >= 60:
        points += 3

    # Vant laget
    points += 1  # Assume won

    return points

# Beregn poeng for alle Barcelona spillere
def calculate_points_for_all_players(player_stats, player_list):
    results = {}
    for player_id in player_list:
        if player_id in player_stats:
            stats = player_stats[player_id]
            points = calculate_points(stats)
            results[player_list[player_id]['name']] = points
        else:
            results[player_list[player_id]['name']] = "No stats available"
    
    return results



