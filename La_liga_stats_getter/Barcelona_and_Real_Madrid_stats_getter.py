import json
import requests


fixtures = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/fixtures/LaLiga_fixture.json"
with open(fixtures, 'r') as file:
    fixture_data = json.load(file)

# Load player data for Barcelona from the API
file_path = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/League_apis/Laliga.json"
with open(file_path, 'r') as file:
    player_data = json.load(file)  # Load the JSON content into a Python dictionary


which_team = input("Which team do you want to gets stats for in La Liga? (Barcelona or Real Madrid)").strip().lower()
if which_team == "barcelona":
    barcelona_club = player_data["La liga"]["Barcelona"]
    team_id = barcelona_club["id"]
    players = barcelona_club["Players"]

elif which_team == "real madrid":
    real_madrid_club = player_data["La liga"]["Real Madrid"]
    team_id = real_madrid_club["id"]
    players = real_madrid_club["Players"]

# Hometeam or awayteam and unavailable players
unavailable_id_list = []

# Load match data
if which_team == "barcelona":
    print("Gameweek 1: Valencia Vs FC Barcelona")
    print("Gameweek 2: FC Barcelona VS Athletic Club")
    print("Gameweek 3: Rayo Vallecano Vs FC Barcelona")
    print("Gameweek 4: FC Barcelona Vs Real Valledolid")
    print("Gameweek 5: Girona Vs FC Barcelona")
    print("Gameweek 6: Villareal Vs FC Barcelona")
    print("Gameweek 7: FC Barcelona Vs Getafe")
    print("Gameweek 8: Osasuna Vs FC Barcelona")
    print("Gameweek 9: Deportivo Alaves Vs FC Barcelona")
    print("gameweek 10: FC Barcelona Vs Sevilla")

elif which_team == "real madrid":
    print("Gameweek 1: Mallorca Vs Real Madrid")
    print("Gameweek 2: Real Valledolid VS Real Madrid")
    print("Gameweek 3: Las Palmas Vs Real Madrid")
    print("Gameweek 4: Real madrid Vs Real Betis")
    print("Gameweek 5: Real Sociadad Vs Real Madrid")
    print("Gameweek 6: Real Madrid Vs Espanyol")
    print("Gameweek 7: Real Madrid Vs deportivo Alaves")
    print("Gameweek 8: Atletico Madrid Vs Real Madrid")
    print("Gameweek 9: Real Madrid Vs villareal")
    print("gameweek 10: Celta Vigo Vs Real Madrid")

gameweek = int(input("Which gameweek do you want to see? "))


last_match_check  = gameweek * 9 + (gameweek - 1)
first_match_check = last_match_check -9
i = first_match_check 

club_name = ""

# Check if there is a match in that gameweek
while i <= last_match_check:

    hometeam = fixture_data[i]["home"]["name"]
    awayteam = fixture_data[i]["away"]["name"]
    hometeam = hometeam.strip().lower()
    awayteam = awayteam.strip().lower()


    if hometeam == which_team:
        club_name = fixture_data[i]["home"]["name"].strip().lower()
        match_id = fixture_data[i]["id"]
        break
    elif awayteam == which_team:
        club_name = fixture_data[i]["away"]["name"].strip().lower()
        match_id = fixture_data[i]["id"]
        break
    else:
        i += 1

print(f"Home team: {hometeam}, Away team: {awayteam}")


if which_team == "barcelona":
    url = 'https://www.fotmob.com/api/matchDetails'
    response = requests.get(url, params={
        'matchId': match_id})
    if response.status_code == 200:
        posts = response.json()
    else:
        print('Error:', response.status_code)

elif which_team == "real madrid":
    url = 'https://www.fotmob.com/api/matchDetails'
    response = requests.get(url, params={
        'matchId': match_id})
    if response.status_code == 200:
        posts = response.json()
    else:
        print('Error:', response.status_code)

if posts["general"]["started"] == "true": 
    print("Kampen har startet")

if which_team == "barcelona":
    match_file = posts

elif which_team == "real madrid":
    match_file = posts

lineup = posts

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


team_stats = posts["content"]["playerStats"]

started = posts["general"]["started"]
finished = posts["general"]["finished"]






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
                    minutes_played = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Minutes played"]["stat"]["value"]
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
                        goals = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Goals"]["stat"]["value"]
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
                        assists = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Assists"]["stat"]["value"]
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
                        passninger_truffet = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["value"]
                        passninger_totalt = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["total"]
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
                        sjanser_skapt = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Chances created"]["stat"]["value"]
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
                        mistet_ballen = posts["content"]["playerStats"][player_id]["stats"][1]["stats"]["Dispossessed"]["stat"]["value"]
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
                        skudd_på_mål = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Total shots"]["stat"]["value"]
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
                        dueler = posts["content"]["playerStats"][player_id]["stats"][3]["stats"]
                        if "Duels won" in dueler:
                            duels_won = posts["content"]["playerStats"][player_id]["stats"][3]["stats"]["Duels won"]["stat"]["value"]
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
                        taklinger_vunnet = posts["content"]["playerStats"][player_id]["stats"][2]["stats"]["Tackles won"]["stat"]["value"]
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
                    minutes_played = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Minutes played"]["stat"]["value"]
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
                    passninger_truffet = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["value"]
                    passninger_totalt = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate passes"]["stat"]["total"]

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
                    lange_passninger_truffet = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate long balls"]["stat"]["value"]
                    lange_passninger_totalt = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Accurate long balls"]["stat"]["total"]
                    if lange_passninger_totalt > 0:
                        lange_passnings_prosent = ((lange_passninger_truffet/lange_passninger_totalt)*100)
                        lange_passnings_prosent = round(lange_passnings_prosent, 2)
                    else:
                        lange_passnings_prosent = 0
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
                    kast = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Throws"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{kast} throws")

                    if kast == 0 or kast <= 7: 
                        keeper_poeng += 0.2
                    elif kast >= 8: 
                        keeper_poeng += 0.35
# Kast
# Diving saves
                    diving_saves = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Diving save"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{diving_saves} diving saves")
                    if diving_saves == 0 or diving_saves == 1: 
                        keeper_poeng += 0.2
                    elif diving_saves >= 2: 
                        keeper_poeng += 0.35
# Diving saves
# Saves inside box
                    saves_inside_box = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Saves inside box"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{saves_inside_box} saves inside the box")
                    if saves_inside_box == 0 or saves_inside_box == 1: 
                        keeper_poeng += 0.2
                    elif saves_inside_box >= 2: 
                        keeper_poeng += 0.35
# Saves inside box
# Act as sweeperkeeper
                    act_as_sweeper = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Acted as sweeper"]["stat"]["value"]
                    if all_stats == True:
                        print(f"{act_as_sweeper} acts as sweeper keeper")
                    if act_as_sweeper == 0: 
                        keeper_poeng += 0 
                    elif act_as_sweeper >= 1: 
                        keeper_poeng += 0.25
# Act as sweeperkeeper
# Punches
                    punches = posts["content"]["playerStats"][player_id]["stats"][0]["stats"]["Punches"]["stat"]["value"]
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

if started == True and finished == True:
    poeng_regning()
else:
    print("Match is not played yet")

