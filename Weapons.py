from Effects import *

#name, power, speed, hitrate, critrate, weapon_range, level
#lower the number, least it has
#power out of 100
#speed out of 10
#weapon range out of 10

# Normal
Rocket_Launcher = Weapon('Rocket Launcher', 40, 1, chance20, chance30, 10, 0)
# Self Harm
Fists = Self_Harm('Fists', 15, 2, chance40, chance10, 1, 0, .50, chance50)
# Multi Shot
Shotgun = Multi_Shot('Shotgun', 5, 3, chance70, chance20, 5, 0, 10)
Daul_Pistols = Multi_Shot('Daul Pistols', 15, 5, chance60, chance10, 8, 0, 2)
Minigun = Multi_Shot('Minigun', 2, 3, chance90, chance30, 8, 0, 20)
# Burn
Flamegun = Burn('Flamegun', 20, 8, chance90, chance20, 4, 0, .50, chance80)
Raygun = Burn('Raygun', 30, 1, chance30, chance30, 5, 0, .50, chance50)
# Zap
Taser = Zap('Taser', 15, 3, chance40, chance20, 3, 0, chance10)
# Bounce
Musket = Bounce('Musket', 20, 2, chance70, chance10, 9, 0, chance50, chance70)
# Headshot
Sniper = Headshot('Sniper', 30, 1, chance80, chance10, 10, 0, chance10)
# Bleed
Sword = Bleed('Sword', 25, 7, chance40, chance10, 2, 0, 0.20, chance60)
Axe = Bleed('Axe', 20, 5, chance40, chance10, 2, 0, 0.30, chance80)
Bow_and_Arrows = Bleed('Bow and Arrows', 15, 4, chance50, chance10, 7, 0, 0.20, chance50)
Throwing_Knife = Bleed('Throwing Knife', 20, 8, chance60, chance10, 6, 0, 0.10, chance30)
# Poison
Blowgun = Poison('Blowgun', 10, 9, chance40, chance10, 4, 0, chance90)
# Curse
Scythe = Curse('Scythe', 20, 8, chance70, chance20, 3, 0, chance90)
# Rage
Club = Rage('Club', 15, 5, chance70, chance10, 2, 0, chance10)