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
print("6. Villareal Vs FC Barcelona")

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
elif which_match == 6: 
    match_file= "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/VillarealVSFCBarcelona.json"
else: 
    print("invalid answar, please choise a number from 1-6!")

with open(match_file, "r") as file:
    lineup = json.load(file)

# Check if Barcelona is the home team
hometeam_id = lineup["content"]["lineup"]["homeTeam"]["id"]

print("")
if hometeam_id == team_id: 
    hometeam = True 
    unavailable = lineup["content"]["lineup"]["homeTeam"]["unavailable"]
else:
    awayteam = True
    unavailable = lineup["content"]["lineup"]["awayTeam"]["unavailable"]

# Add unavailable player IDs to list
for player in unavailable:
    unavailable_id_list.append(player["id"])

hometeam_score = lineup["header"]["teams"][0]["score"]
awayteam_score = lineup["header"]["teams"][1]["score"]





def poeng_regning(): 
    # Check if Barcelona is the home team
    hometeam_id = lineup["content"]["lineup"]["homeTeam"]["id"]

    if hometeam_id == team_id: 
        hometeam = 0
        awayteam = 10
        unavailable = lineup["content"]["lineup"]["homeTeam"]["unavailable"]
    else:
        awayteam = 1
        hometeam = 10
        unavailable = lineup["content"]["lineup"]["awayTeam"]["unavailable"]

    # Add unavailable player IDs to list
    for player in unavailable:
        unavailable_id_list.append(player["id"])

    hometeam_score = lineup["header"]["teams"][0]["score"]
    awayteam_score = lineup["header"]["teams"][1]["score"]



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
                print(f"Player ID: {player_id}, Name: {player_info['name']}")
                position = player_info["position"]
                if position == 10: 
                    spiller_poeng = 0
                    
# minutes played
                    minutes_played = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Minutes played"]["stat"]["value"]
                    print(f"{minutes_played} minutes")
                    if minutes_played >= 60: 
                        spiller_poeng += 3
                    else: 
                        spiller_poeng += 1
# Minutes played
# Goals
                    goals = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Goals"]["stat"]["value"]
                    print(f"{goals} goals")
                    if goals == 1: 
                        spiller_poeng += 1
                    elif goals == 2: 
                        spiller_poeng += 1.5
                    elif goals >= 3: 
                        spiller_poeng += 2
                    else: 
                        spiller_poeng += 0
# Goals
# Assist
                    assists = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Assists"]["stat"]["value"]
                    print(f"{assists} assists")
                    if assists == 1: 
                        spiller_poeng += 1
                    elif assists == 2: 
                        spiller_poeng += 1.5
                    elif assists >= 3: 
                        spiller_poeng += 2
                    else: 
                        spiller_poeng += 0
# Assist
# Passning
                    passninger_truffet = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["value"]
                    passninger_totalt = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["total"]
                    passning_prosent = ((passninger_truffet/passninger_totalt)*100)
                    passning_prosent = round(passning_prosent, 2)
                    print(f"{passning_prosent} % passningsprosent")
                    if passning_prosent <= 20: 
                        spiller_poeng += 0.2
                    elif passning_prosent <= 40 and passning_prosent > 20: 
                        spiller_poeng += 0.4
                    elif passning_prosent <= 60 and passning_prosent > 40: 
                        spiller_poeng += 0.6
                    elif passning_prosent <= 80 and passning_prosent > 60: 
                        spiller_poeng += 0.8
                    elif passning_prosent <= 100 and passning_prosent > 80: 
                        spiller_poeng += 1

# Passing
# Sjanser skapt
                    sjanser_skapt = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Chances created"]["stat"]["value"]
                    print(f"{sjanser_skapt} sjanse(r) skapt")
                    if sjanser_skapt <= 1: 
                        spiller_poeng += 0.4
                    elif sjanser_skapt == 2 or sjanser_skapt == 3: 
                        spiller_poeng += 0.6
                    elif sjanser_skapt >= 4: 
                        spiller_poeng += 1


# Sjanser skapt
# Mistet ballen
                    mistet_ballen = stats["content"]["playerStats"][player_id]["stats"][1]["stats"]["Dispossessed"]["stat"]["value"]
                    print(f"Mistet ballen:{mistet_ballen}")
                    if mistet_ballen >= 1:
                        spiller_poeng += 0
                    elif mistet_ballen == 2 or mistet_ballen == 3: 
                        spiller_poeng -= 0.1
                    elif mistet_ballen == 4 or mistet_ballen == 5: 
                        spiller_poeng -= 0.2
                    elif mistet_ballen > 5: 
                        spiller_poeng -= 0.3
# Mistet ballen
# Skudd på mål
                    skudd_på_mål = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Total shots"]["stat"]["value"]
                    print(f"{skudd_på_mål} skudd på mål")
                    if skudd_på_mål == 1:
                        spiller_poeng += 0
                    elif skudd_på_mål == 2 or skudd_på_mål == 3: 
                        spiller_poeng += 0.3
                    elif skudd_på_mål == 4 or skudd_på_mål == 5: 
                        spiller_poeng += 0.5
                    elif skudd_på_mål > 5: 
                        spiller_poeng += 0.75
# Skudd på mål
# Duels won 
                    dueler = stats["content"]["playerStats"][player_id]["stats"][3]["stats"]
                    if "Duels won" in dueler:
                        duels_won = stats["content"]["playerStats"][player_id]["stats"][3]["stats"]["Duels won"]["stat"]["value"]
                        print(f"{duels_won} dueler vunnet")
                        if duels_won <= 2: 
                            spiller_poeng += 0.3
                        elif duels_won > 2 and duels_won <= 4: 
                            spiller_poeng += 0.6
                        elif duels_won >= 5: 
                            spiller_poeng += 1

                    else: 
                        print("Dueler vunnet: Ikke tilgjenglig")
# Duels won 
# Taklinger vunnet
                    taklinger_vunnet = stats["content"]["playerStats"][player_id]["stats"][2]["stats"]["Tackles won"]["stat"]["value"]
                    print(f"{taklinger_vunnet} takligner funnet")
                    if taklinger_vunnet <= 2: 
                        spiller_poeng += 0.2
                    elif taklinger_vunnet > 2 and taklinger_vunnet < 4: 
                        spiller_poeng += 0.4
                    elif taklinger_vunnet >= 5: 
                        spiller_poeng += 0.6
# Taklinger vunnet 
# Cleansheet
                    if hometeam == 0: 
                        if awayteam_score == 0: 
                            print("Cleansheet")
                            spiller_poeng += 0.5
                        else: 
                            print("Ikke cleensheet")
                    elif awayteam == 1: 
                        if hometeam_score == 0: 
                            print("Cleansheet")
                            spiller_poeng += 0.5
                        else: 
                            print("Ikke cleansheet")
# Cleansheet
# Poeng for utespillere
                    if minutes_played < 10: 
                        print("Spiller spilte for lite tid til å kalkulere poeng")
                    else: 
                        spiller_poeng = round(spiller_poeng, 2)
                        print(f"{spiller_poeng} poeng")
# Poeng for utespillere

# Keeper
                elif position == 1: 
                    print("Keeper")
                    keeper_poeng = 0
# Minutter
                    minutes_played = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Minutes played"]["stat"]["value"]
                    print(f"{minutes_played} minutter")
                    if minutes_played >= 60: 
                        keeper_poeng += 3
                    else: 
                        keeper_poeng += 1
# Minutter
# Mål sluppet inn
                    if hometeam == 0: 
                        if awayteam_score == 0: 
                            print("Cleansheet")
                            keeper_poeng += 2
                        else: 
                            print("Ikke cleensheet")
                            if awayteam_score == 1 or awayteam_score == 2: 
                                keeper_poeng -= 0.25
                            elif awayteam_score == 3 or awayteam_score == 4: 
                                keeper_poeng -= 0.5
                            elif hometeam_score >= 5: 
                                keeper_poeng -= 0.85

                    elif awayteam == 1: 
                        if hometeam_score == 0: 
                            print("Cleansheet")
                            keeper_poeng += 2
                        else: 
                            print("Ikke cleansheet")
                            if hometeam_score == 1 or hometeam_score == 2: 
                                keeper_poeng -= 0.25
                            elif hometeam_score == 3 or hometeam_score == 4: 
                                keeper_poeng -= 0.5
                            elif hometeam_score >= 5: 
                                keeper_poeng -= 0.85


# Mål sluppet inn 
            
                    
                    
                    print(f"{keeper_poeng} poeng")
# Keeper
            

                
                print("")
        else:
            print(f"No stats available for Player ID: {player_id}, Name: {player_info['name']}")
            print("")

poeng_regning()


