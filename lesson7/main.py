import time
import random
from colorama import Fore
import os
from lesson7.entity import Player, Monster
from lesson7.game import *

print("Добро пожаловать в игру про драки с монстром!")

delay = 3
count_move = 0

#Выбор игрока атака или защита
def player_chose():
    variants = ["защита", "атака"]
    while True:
        player_choice = input("Что ты выберешь(защита/атака)? ").lower()
        if player_choice in variants or player_choice == "выход":
            break
        else:
            print("Такого варианта нет!")
    monster_choice = random.choice(variants)
    return player_choice, monster_choice

#Проверка об окончание игры
def check_game_over(player, monster):
    if player.health <= 0:
        print(Fore.RED + "Ты погиб!" + Fore.RESET)
        print(Fore.YELLOW + "МОНСТР WINS!!!" + Fore.RESET)
        return True
    if monster.health <= 0:
        print(Fore.GREEN + "Монстр погиб!" + Fore.RESET)
        print(Fore.YELLOW + "ТЫ WINS!!!" + Fore.RESET)
        return True
    return False

#Проверка выборов игроков и дальнейшая обработка
def check_attack(player, player_choice, monster, monster_choice):
    global count_move
    if player_choice == "защита":
        if monster_choice == "защита":
            print("Два дурачка стоят и защищаются! Ахахахах!")
        else:
            print(f"Ты защищаешься (armor: {player.armor})")
            print(f"Монстр атакует! (damage: {monster.damage})")
            print(f"Ты получил урон: {player.defense(monster)}")
    else:
        if monster_choice == "защита":
            print(f"Ты атакуешь! (damage: {player.damage})")
            print(f"Монстр защищается! (armor: {monster.armor})")
            print(f"Монстр получил урон: {player.attack(monster)}")
        else:
            print(f"Ты атакуешь! (damage: {player.damage})")
            print(f"Монстр атакует! (damage: {monster.damage})")
            print(f"Ты получил урон: {player.defense(monster)}")
            print(f"Монстр получил урон: {player.attack(monster)}")
    count_move += 1
    write_save_file(player.health, monster.health, count_move)

#Основной цикл игры
def main_cycle():
    player = Player(random.randint(0, 10), random.randint(0, 10))
    monster = Monster(random.randint(0, 10), random.randint(0, 10))

    if os.path.isfile("save.json"):
        user_input = input("Обнаружен файл с сохранение, хотите его загрузить? ").lower()
        if user_input == "да":
            player.health, monster.health = read_for_file()

    while True:
        player.damage, player.armor = random.randint(70, 80), random.randint(0, 1)
        monster.damage, monster.armor = random.randint(70, 80), random.randint(0, 1)
        if check_game_over(player, monster):
            break
        print("Твоё здоровье:", player.health)
        print("Здоровье монстра:", monster.health, "\n")

        player_choice, monster_choice = player_chose()
        check_attack(player, player_choice, monster, monster_choice)

        time.sleep(delay)


if __name__ == "__main__":
    main_cycle()
    print("Конец игры!")