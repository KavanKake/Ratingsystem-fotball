if which_team == "barcelona":
    Barcelona = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Matchdays_LaLiga/Barcelona_kamper.json"
    with open(Barcelona, 'r') as file:
        matchdays = json.load(file)

elif which_team == "real madrid":
    Real_Madrid = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/Matchdays_LaLiga/Real_Madrid_kamper.json"
    with open(Real_Madrid, 'r') as file:
        matchdays = json.load(file)

if gameweek == 1:
    match_id = matchdays["Matchdays"]["1"]
elif gameweek == 2:
    match_id = matchdays["Matchdays"]["2"]
elif gameweek == 3:
    match_id = matchdays["Matchdays"]["3"]
elif gameweek == 4:
    match_id = matchdays["Matchdays"]["4"]
elif gameweek == 5:
    match_id = matchdays["Matchdays"]["5"]
elif gameweek == 6:
    match_id = matchdays["Matchdays"]["6"]
elif gameweek == 7:
    match_id = matchdays["Matchdays"]["7"]
elif gameweek == 8:
    match_id = matchdays["Matchdays"]["8"]
elif gameweek == 9:
    match_id = matchdays["Matchdays"]["9"]
elif gameweek == 10:
    match_id = matchdays["Matchdays"]["10"]