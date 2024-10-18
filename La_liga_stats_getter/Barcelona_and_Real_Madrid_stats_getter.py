import json


# Load player data for Barcelona from the API
file_path = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/League_apis/Laliga.json"
with open(file_path, 'r') as file:
    player_data = json.load(file)  # Load the JSON content into a Python dictionary



which_team = input("Which team do you want to gets stats for in La Liga? (Barcelona or Real Madrid) ")
if which_team == "Barcelona":
    barcelona_club = player_data["La liga"]["Barcelona"]
    team_id = barcelona_club["id"]
    players = barcelona_club["Players"]

elif which_team == "Real Madrid":
    real_madrid_club = player_data["La liga"]["Real Madrid"]
    team_id = real_madrid_club["id"]
    players = real_madrid_club["Players"]



# Hometeam or awayteam and unavailable players
unavailable_id_list = []

# Load match data
if which_team == "Barcelona":
    print("Gameweek 1: Valencia Vs FC Barcelona")
    print("Gameweek 2: FC Barcelona VS Athletic Club")
    print("Gameweek 3: Rayo Vallecano Vs FC Barcelona")
    print("Gameweek 4: FC Barcelona Vs Real Valledolid")
    print("Gameweek 5: Girona Vs FC Barcelona")
    print("Gameweek 6: Villareal Vs FC Barcelona")
    print("Gameweek 7: FC Barcelona Vs Getafe")
    print("Gameweek 8: Osasuna Vs FC Barcelona")
    print("Gameweek 9: Deportivo Alaves Vs FC Barcelona")

elif which_team == "Real Madrid":
    print("Gameweek 1: Mallorca Vs Real Madrid")
    print("Gameweek 2: Real Valledolid VS Real Madrid")
    print("Gameweek 3: Las Palmas Vs Real Madrid")
    print("Gameweek 4: Real madrid Vs Real Betis")
    print("Gameweek 5: Real Sociadad Vs Real Madrid")



which_match = int(input("Which gameweek do you want to see?"))

if which_team == "Barcelona":
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
    elif which_match == 7:
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/BarcelonaVSGetafe.json"
    elif which_match == 8:
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/OsasunaVSBarcelona.json"
    elif which_match == 9:
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Barcelona_apis/DeportivoAlavesVSBarcelona.json"
    else: 
        print("invalid answar, please choise a number from 1-9!")

elif which_team == "Real Madrid":
    if which_match == 1: 
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Real_madrid_apis/MallorcaVSRealMadrid.json"
    elif which_match == 5: 
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Real_madrid_apis/RealSociadadVSRealMadrid.json"
    elif which_match == 3: 
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Real_madrid_apis/LasPalmasVSRealMadrid.json"
    elif which_match == 4: 
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Real_madrid_apis/RealMadridVSRealBetis.json"
    elif which_match == 2: 
        match_file = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Real_madrid_apis/RealMadridVSRealValledolid.json"
    else:
        print("invalid answar, please choise a number from 1-5!")

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

with open(match_file, "r") as file:
    stats = json.load(file)
team_stats = stats["content"]["playerStats"]




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

    yellow_card = []
    red_card = []

    if hometeam == 0: 
        for player in lineup["content"]["lineup"]["homeTeam"]["starters"]:
            events = player["performance"].get("events", [])
            for event in events:
                if event["type"] == "yellowCard":
                    yellow_card.append(player["id"])
                elif event["type"] == "redCard":
                    red_card.append(player["id"])
    elif awayteam == 1: 
        for player in lineup["content"]["lineup"]["awayTeam"]["starters"]:
            events = player["performance"].get("events", [])
            for event in events:
                if event["type"] == "yellowCard":
                    yellow_card.append(player["id"])
                elif event["type"] == "redCard":
                    red_card.append(player["id"])
    

    all_stats = input("Would you like to see all stats? (y/n)")
    if all_stats == "y":
        all_stats = True
    else: 
        all_stats = False



    # Iterate over Barcelona players and print stats for available players
    for player_id, player_info in players.items():
        # Skip players if they are in the unavailable list
        if player_id in unavailable_id_list:
            continue  # Skip this player
        
        # Load match stats
        

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
                    if all_stats == True:
                        print(f"{minutes_played} minutes")

                    if minutes_played < 10: 
                        print("Spiller spilte mindre enn 10 minutter, og poeng ble ikke generert")
                    else:
                        if minutes_played >= 60: 
                            spiller_poeng += 3
                        else: 
                            spiller_poeng += 1
# Minutes played
# Goals
                        goals = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Goals"]["stat"]["value"]
                        if all_stats == True:
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
                        if all_stats == True:
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
                        if all_stats == True:
                            print(f"{passning_prosent} % passing accuracy")
                        
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
                        if all_stats == True:
                            print(f"{sjanser_skapt} chances created")
                        if sjanser_skapt <= 1: 
                            spiller_poeng += 0.4
                        elif sjanser_skapt == 2 or sjanser_skapt == 3: 
                            spiller_poeng += 0.6
                        elif sjanser_skapt >= 4: 
                            spiller_poeng += 1
# Sjanser skapt
# Mistet ballen
                        mistet_ballen = stats["content"]["playerStats"][player_id]["stats"][1]["stats"]["Dispossessed"]["stat"]["value"]
                        if all_stats == True:
                            print(f"Dispossessed:{mistet_ballen}")
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
                        if all_stats == True:
                            print(f"{skudd_på_mål} shot at goal")
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
                            if all_stats == True:    
                                print(f"{duels_won} dueler won")
                            if duels_won <= 2: 
                                spiller_poeng += 0.3
                            elif duels_won > 2 and duels_won <= 4: 
                                spiller_poeng += 0.6
                            elif duels_won >= 5: 
                                spiller_poeng += 1

                        else:
                            if all_stats == True: 
                                print("Dueler vunnet: Ikke tilgjenglig")
# Duels won 
# Taklinger vunnet
                        taklinger_vunnet = stats["content"]["playerStats"][player_id]["stats"][2]["stats"]["Tackles won"]["stat"]["value"]
                        if all_stats == True:
                            print(f"{taklinger_vunnet} tackles won")
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
                                if all_stats == True:
                                    print("Cleansheet")
                                spiller_poeng += 0.5
                            else: 
                                if all_stats == True:
                                    print("Not cleensheet")
                        elif awayteam == 1: 
                            if hometeam_score == 0: 
                                if all_stats == True:
                                    print("Cleansheet")
                                spiller_poeng += 0.5
                            else: 
                                if all_stats == True:
                                    print("Not cleansheet")
# Cleansheet
# Diseplin
                        if player_id in str(yellow_card): 
                            print("Player got yellow card")
                            spiller_poeng -= 0.5
                        elif player_id in str(red_card):
                            print("player got red card")
                            spiller_poeng -= 1
                        else: 
                            print("no card")
# Diseplin

# Poeng for utespillere
                        if minutes_played < 10: 
                            print("Not enough time to calculate")
                        else: 
                            spiller_poeng = round(spiller_poeng, 2)
                            print(f"{spiller_poeng} points")
# Poeng for utespillere

# Keeper
                elif position == 1: 
                    print("Keeper")
                    keeper_poeng = 0
# Minutter
                    minutes_played = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Minutes played"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{minutes_played} minutes")
                    if minutes_played >= 60: 
                        keeper_poeng += 3
                    else: 
                        keeper_poeng += 1
# Minutter
# Mål sluppet inn
                    if hometeam == 0: 
                        if awayteam_score == 0:
                            if all_stats == True: 
                                print("Cleansheet")
                            keeper_poeng += 2
                        else:
                            if all_stats == True: 
                                print("Not cleensheet")
                            if awayteam_score == 1 or awayteam_score == 2: 
                                keeper_poeng -= 0.25
                            elif awayteam_score == 3 or awayteam_score == 4: 
                                keeper_poeng -= 0.5
                            elif hometeam_score >= 5: 
                                keeper_poeng -= 0.85

                    elif awayteam == 1: 
                        if hometeam_score == 0: 
                            if all_stats == True:
                                print("Cleansheet")
                            keeper_poeng += 2
                        else: 
                            if all_stats == True:    
                                print("Not cleansheet")
                            if hometeam_score == 1 or hometeam_score == 2: 
                                keeper_poeng -= 0.25
                            elif hometeam_score == 3 or hometeam_score == 4: 
                                keeper_poeng -= 0.5
                            elif hometeam_score >= 5: 
                                keeper_poeng -= 0.85
# Mål sluppet inn 
# Passnings prosent
                    passninger_truffet = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["value"]
                    passninger_totalt = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["total"]

                    passning_prosent = ((passninger_truffet/passninger_totalt)*100)
                    passning_prosent = round(passning_prosent, 2)
                    if all_stats == True:
                        print(f"{passning_prosent} % passing accuracy")

                    if passning_prosent <= 20: 
                        keeper_poeng += 0.1
                    elif passning_prosent <= 40 and passning_prosent > 20: 
                        keeper_poeng += 0.2
                    elif passning_prosent <= 60 and passning_prosent > 40: 
                        keeper_poeng += 0.3
                    elif passning_prosent <= 80 and passning_prosent > 60: 
                        keeper_poeng += 0.4
                    elif passning_prosent <= 100 and passning_prosent > 80: 
                        keeper_poeng += 0.5
# Passnings prosent             
# Lange passnings prosent
                    lange_passninger_truffet = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate long balls"]["stat"]["value"]
                    lange_passninger_totalt = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate long balls"]["stat"]["total"]

                    lange_passnings_prosent = ((lange_passninger_truffet/lange_passninger_totalt)*100)
                    lange_passnings_prosent = round(lange_passnings_prosent, 2)
                    if all_stats == True:
                        print(f"{lange_passnings_prosent} % longball prosent")

                    if lange_passnings_prosent <= 20: 
                        keeper_poeng += 0.1
                    elif lange_passnings_prosent <= 40 and lange_passnings_prosent > 20: 
                        keeper_poeng += 0.2
                    elif lange_passnings_prosent <= 60 and lange_passnings_prosent > 40: 
                        keeper_poeng += 0.3
                    elif lange_passnings_prosent <= 80 and lange_passnings_prosent > 60: 
                        keeper_poeng += 0.4
                    elif lange_passnings_prosent <= 100 and lange_passnings_prosent > 80: 
                        keeper_poeng += 0.5
# Lange passnings prosent
# Kast
                    kast = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Throws"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{kast} throws")

                    if kast == 0 or kast <= 7: 
                        keeper_poeng += 0.2
                    elif kast >= 8: 
                        keeper_poeng += 0.35
# Kast
# Diving saves
                    diving_saves = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Diving save"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{diving_saves} diving saves")
                    if diving_saves == 0 or diving_saves == 1: 
                        keeper_poeng += 0.2
                    elif diving_saves >= 2: 
                        keeper_poeng += 0.35
# Diving saves
# Saves inside box
                    saves_inside_box = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Saves inside box"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{saves_inside_box} saves inside the box")
                    if saves_inside_box == 0 or saves_inside_box == 1: 
                        keeper_poeng += 0.2
                    elif saves_inside_box >= 2: 
                        keeper_poeng += 0.35
# Saves inside box
# Act as sweeperkeeper
                    act_as_sweeper = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Acted as sweeper"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{act_as_sweeper} acts as sweeper keeper")
                    if act_as_sweeper == 0: 
                        keeper_poeng += 0 
                    elif act_as_sweeper >= 1: 
                        keeper_poeng += 0.25
# Act as sweeperkeeper
# Punches
                    punches = stats["content"]["playerStats"][player_id]["stats"][0]["stats"]["Punches"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{punches} punches")
                    if punches <= 3: 
                        keeper_poeng += 0.2
                    elif punches >= 4: 
                        keeper_poeng += 0.3
# Punches
# Diseplin
                    if player_id in str(yellow_card): 
                        print("Player got yellow card")
                        keeper_poeng -= 0.5
                    elif player_id in str(red_card):
                        print("player got red card")
                        keeper_poeng -= 1
                    else: 
                        print("no card")
# Diseplin
                    keeper_poeng = round(keeper_poeng, 2)
                    print(f"{keeper_poeng} poeng")
# Keeper
            

                
                print("")
        else:
            print(f"No stats available for Player ID: {player_id}, Name: {player_info['name']}")
            print("")

poeng_regning()


