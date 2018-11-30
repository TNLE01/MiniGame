# Heros

class Hero:

    def __init__(self, name, health, speed, armor, weapon, typeof):
        self.name = name
        self.health = health
        self.speed = speed
        self.armor = armor
        self.weapon = weapon
        self.typeof = typeof

    def test(self):
        print(self.name)
        print(self.health)
        print(self.speed)
        print(self.armor)
        print(self.weapon)


class Fire(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, FP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.FP = FP


class Water(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, WP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.WP = WP


class Ice(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, IP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.IP = IP


class Earth(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, EP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.EP = EP


class Wind(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, AP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.AP = AP


class Nature(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, NP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.NP = NP


class Lightning(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, LP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.LP = LP


class Ghost(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof, GP):
        super().__init__(name, health, speed, armor, weapon, typeof)
        self.GP = GP


# Maps

class Area:

  def __init__(self, name, damage, power, hitrate, typeof):
    self.name = name
    self.damage = damage
    self.power = power
    self.hitrate = hitrate
    self.type = typeof


# Monsters

class Monster(Hero):

    def __init__(self, name, health, speed, armor, weapon, typeof):
        super().__init__(name, health, speed, armor, weapon, typeof)