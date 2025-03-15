#Абстрактное представление существа
class Entity:
    def __init__(self, damage, armor):
        self._damage = damage
        self._armor = armor
        self._health = 100

    @staticmethod
    def check_damage_limit(damage):
        if damage < 0:
            return 0
        return damage

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, armor):
        self._armor = armor

    @property
    def health(self):
        if self._health <= 0:
            return 0
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

#Класс игрока
class Player(Entity):
    def attack(self, monster):
        damage = self.check_damage_limit(self._damage - monster.armor)
        monster.health -= damage
        return damage

    def defense(self, monster):
        damage = self.check_damage_limit(monster.damage - self.armor)
        self.health -= damage
        return damage

#Класс монстра
class Monster(Entity):
    pass