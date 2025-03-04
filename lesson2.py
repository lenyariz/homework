herbs = int(input("Сколько травы добавить: "))
crystals = int(input("Сколько добавить кристаллов: "))
water = int(input("Сколько добавить воды: "))
fire_dust = int(input("Сколько огненной пыли добавить: "))
moonlight = int(input("Сколько лунного света добавить: "))

temp_power = herbs + crystals + water + fire_dust + moonlight > 150
magic_power = (herbs * 0.5 + crystals * 1.5 + water * 0.8 + fire_dust * 1.0 + moonlight * 1.2) + (20 * temp_power)


