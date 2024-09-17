for player_id, player_info in barcelona_players.items():
    # Skip players if they are in the unavailable list

    
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