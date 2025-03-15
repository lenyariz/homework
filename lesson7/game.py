import json


def write_save_file(player_health, monster_health, count_move):
    with open("save.json", "w") as file:
        json.dump({"player_health": player_health, "monster_health": monster_health, "count_move": count_move}, file)


def read_for_file():
    with open("save.json", "r") as file:
        data = json.load(file)
        return data["player_health"], data["monster_health"]