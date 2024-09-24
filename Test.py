import json

# JSON data
data = {
    "93447": {
        "name": "Robert Lewandowski",
        "stats": [
            {
                "title": "Top stats",
                "key": "top_stats",
                "stats": {
                    "FotMob rating": {
                        "key": "rating_title",
                        "stat": {
                            "value": 8.64,
                            "type": "double"
                        }
                    },
                    "Minutes played": {
                        "key": "minutes_played",
                        "stat": {
                            "value": 90,
                            "type": "integer"
                        }
                    },
                    "Goals": {
                        "key": "goals",
                        "stat": {
                            "value": 2,
                            "type": "integer"
                        }
                    },
                    "Assists": {
                        "key": "assists",
                        "stat": {
                            "value": 0,
                            "type": "integer"
                        }
                    },
                    "Total shots": {
                        "key": "total_shots",
                        "stat": {
                            "value": 4,
                            "type": "integer"
                        }
                    },
                    "Shotmap": {
                        "key": None,
                        "stat": {
                            "value": True
                        }
                    },
                    "Accurate passes": {
                        "key": "accurate_passes",
                        "stat": {
                            "value": 16,
                            "total": 21,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Chances created": {
                        "key": "chances_created",
                        "stat": {
                            "value": 0,
                            "type": "integer"
                        }
                    },
                    "Missed penalty": {
                        "key": "missed_penalty",
                        "stat": {
                            "value": 1,
                            "type": "integer"
                        }
                    },
                    "Expected goals (xG)": {
                        "key": "expected_goals",
                        "stat": {
                            "value": 2.49,
                            "type": "double"
                        }
                    },
                    "Expected goals on target (xGOT)": {
                        "key": "expected_goals_on_target_variant",
                        "stat": {
                            "value": 2.07,
                            "type": "double"
                        }
                    },
                    "Expected assists (xA)": {
                        "key": "expected_assists",
                        "stat": {
                            "value": 0.02,
                            "type": "double"
                        }
                    },
                    "xG + xA": {
                        "key": "xg_and_xa",
                        "stat": {
                            "value": 2.51,
                            "type": "double"
                        }
                    }
                }
            },
            {
                "title": "Attack",
                "key": "attack",
                "stats": {
                    "Shot accuracy": {
                        "key": "shot_accuracy",
                        "stat": {
                            "value": 3,
                            "total": 4,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Big chances missed": {
                        "key": "big_chance_missed_title",
                        "stat": {
                            "value": 2,
                            "type": "integer"
                        }
                    },
                    "Touches": {
                        "key": "touches",
                        "stat": {
                            "value": 34,
                            "type": "integer"
                        }
                    },
                    "Touches in opposition box": {
                        "key": "touches_opp_box",
                        "stat": {
                            "value": 6,
                            "type": "integer"
                        }
                    },
                    "Successful dribbles": {
                        "key": "dribbles_succeeded",
                        "stat": {
                            "value": 3,
                            "total": 3,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Accurate long balls": {
                        "key": "long_balls_accurate",
                        "stat": {
                            "value": 2,
                            "total": 3,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Dispossessed": {
                        "key": "dispossessed",
                        "stat": {
                            "value": 3,
                            "type": "integer"
                        }
                    },
                    "xG Non-penalty": {
                        "key": "expected_goals_non_penalty",
                        "stat": {
                            "value": 1.7,
                            "type": "double"
                        }
                    }
                }
            },
            {
                "title": "Defense",
                "key": "defense",
                "stats": {
                    "Tackles won": {
                        "key": "tackles_succeeded",
                        "stat": {
                            "value": 0,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Defensive actions": {
                        "key": "defensive_actions",
                        "stat": {
                            "value": 0,
                            "type": "integer"
                        }
                    },
                    "Recoveries": {
                        "key": "recoveries",
                        "stat": {
                            "value": 3,
                            "type": "integer"
                        }
                    }
                }
            },
            {
                "title": "Duels",
                "key": "duels",
                "stats": {
                    "Duels won": {
                        "key": "duel_won",
                        "stat": {
                            "value": 3,
                            "type": "integer"
                        }
                    },
                    "Duels lost": {
                        "key": "duel_lost",
                        "stat": {
                            "value": 3,
                            "type": "integer"
                        }
                    },
                    "Ground duels won": {
                        "key": "ground_duels_won",
                        "stat": {
                            "value": 3,
                            "total": 6,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Aerial duels won": {
                        "key": "aerials_won",
                        "stat": {
                            "value": 0,
                            "total": 0,
                            "type": "fractionWithPercentage"
                        }
                    },
                    "Was fouled": {
                        "key": "was_fouled",
                        "stat": {
                            "type": "integer"
                        }
                    },
                    "Fouls committed": {
                        "key": "fouls",
                        "stat": {
                            "type": "integer"
                        }
                    }
                }
            }
        ]
    }
}

# Extracting the minutes played
minutes_played = data["93447"]["stats"][0]["stats"]["Minutes played"]["stat"]["value"]

# Printing the result
print(f"Minutes played: {minutes_played}")
