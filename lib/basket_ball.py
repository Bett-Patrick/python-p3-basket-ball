def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


#Solutions:
game_data = game_dict()

# function to return a player's number of points per game
def num_points_per_game(player_name): 
    for player in game_data["home"]["players"] + game_data["away"]["players"]:
        if player["name"].lower() == player_name.lower():
            return (f"{player['name']}'s points per game: {player['points_per_game']}")
    return (f"{player_name} is not {game_data['home']['team_name']}'s or {game_data['away']['team_name']}'s player")

                # Test cases:
# from home team
print(num_points_per_game("Jarrett Allen"))
# from away team
print(num_points_per_game("Rui Hachimura"))
# from neither teams
print(num_points_per_game("Patrick Bett"))


# function to return player's age
def player_age(player_name):
    for player in game_data["home"]["players"] + game_data["away"]["players"]:
        if player["name"].lower() == player_name.lower():
            return (f"{player['name']}'s age: {player['age']}")
    return (f"{player_name} is not {game_data['home']['team_name']}'s or {game_data['away']['team_name']}'s player")

                # Test cases:
# from home team
print(player_age("Jarrett Allen"))
# from away team
print(player_age("Rui Hachimura"))
# from neither teams
print(player_age("Patrick Bett"))


# function to return team's colors
def team_colors(team_name):
    for team in [game_data["home"], game_data["away"]]:
        if team["team_name"].lower() == team_name.lower():
            return f"{team['team_name']}'s colors:\n\t{(team['colors'])}"
    return "Team not available"

                # Test cases:
# home team
print(team_colors("Cleveland Cavaliers"))
# away team
print(team_colors("Washington Wizards"))
# from neither teams
print(team_colors("Patrick Bett"))

#function to return a list of team names
def team_names():
    return [game_data["home"]["team_name"],game_data["away"]["team_name"]]

# Test cases
print(f"Home and Away teams:\n\t{team_names()}")

#function to return a list of team jerseys

def player_numbers(team_name):
    teams = team_names()
    team_jerseys = []
    if team_name.lower() == teams[0].lower():
        for player in game_data["home"]["players"]:
            team_jerseys.append(player["number"])
        return (f"Home team's jersey numbers:\n\t{team_jerseys}")
    elif team_name.lower() == teams[1].lower():
        for player in game_data["away"]["players"]:
            team_jerseys.append(player["number"])
        return (f"Away team's jersey numbers:\n\t{team_jerseys}")
    else:
        return "Team not available!!"

            # Test cases
# home team
print(player_numbers("Cleveland Cavaliers"))
# away team
print(player_numbers("Washington Wizards"))
# from neither teams
print(player_numbers("Patrick Bett"))


#function to display player's stats
def player_stats(player_name):
    for player in game_data["home"]["players"] + game_data["away"]["players"]:
        if player["name"].lower() == player_name.lower():
            return (f"{player['name']}'s stats:\n  {player}")

# Test cases
print(player_stats("Darius Garland"))


# CHALLENGE
# finding average number of rebounds for players who wear a particular shoe brand.

# function to create a dictionary of rebounds per shoe brand
def create_brand_dict(brand_name):
    shoe_brand_rebounds = {}
    for player in game_data["home"]["players"] + game_data["away"]["players"]:
        if player["shoe_brand"] == brand_name:
            rebounds = player["rebounds_per_game"]
            if brand_name not in shoe_brand_rebounds:
                shoe_brand_rebounds[brand_name] = []
            shoe_brand_rebounds[brand_name].append(rebounds)
    # shoe_brand_rebounds.clear()
    # print(f"cleared:\n\t{shoe_brand_rebounds}")
    return shoe_brand_rebounds

print(create_brand_dict("Nike"))

#function to calculate average rebounds by shoe brand
def average_rebounds_by_shoe_brand(brand_name):
    shoe_brand_rebounds = create_brand_dict(brand_name)
    for brand, rebounds_list in shoe_brand_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        return(f"{brand}: {average_rebounds:.2f}")

print(average_rebounds_by_shoe_brand("Nike"))
print(average_rebounds_by_shoe_brand("Adidas"))

