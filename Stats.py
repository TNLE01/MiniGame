from Functions import *
from GameItems import *
from Weapons import *

# Heros


# Area
# None
Hellion_Arena = Area('Hellion_Arena', 'no', 0, chance0, 'none')
# Fire
Diablo_Pinnacle = Area('Diablo Pinnacle', 'yes', 80, chance70, 'fire')
# Water
White_Gorge = Area('White Gorge', 'no', 0, chance0,'water')
# Ice
Frozen_Drumlins = Area('Frozen Drumlins', 'no', 0, chance0,'ice')
# Earth
Drumlins = Area('Drumlins', 'no', 0, chance0,'earth')
# Wind
Icarus_Stadium = Area('Icarus Stadium', 'no', 0, chance0,'wind')
Forsaken_Apex = Area('Forsaken Apex', 'yes', 10, chance90,'wind')
# Nature
Dark_Woods = Area('Dark Woods', 'yes', 5, chance90,'nature')
# Lightning
Catatumbo_River = Area('Catatumbo River', 'yes', 50, chance80,'lightning')
# Ghost
Lunaland = Area('Lunaland', 'yes', 10, chance20,'ghost')
Forest_of_Stone = Area('Forest of Stone', 'yes', 20, chance30,'ghost')
Shore_of_Silence = Area('Shore of Silence', 'yes', 40, chance50,'ghost')

# Monsters
# None
Bigfoot = Monster('Bigfoot', 150, 6, 0, Club, 'none')
Orc = Monster('Orc', 200, 4, 50, Sword, 'none')
# Fire
Fire_Demon = Monster('Fire Demon', 200, 4, 0, Flamegun, 'fire')
# Water
Kraken = Monster('Kraken', 300, 6, 0, Fists, 'water')
# Ice
Yeti = Monster('Yeti', 150, 5, 0, Club, 'ice')
Ice_Golem = Monster('Ice Golem', 250, 2, 0, Fists, 'ice')
# Earth
Zombie = Monster('Zombie', 100, 3, 0, Fists, 'earth')
Mummy = Monster('Mummy', 100, 5, 0, Fists, 'earth')
Rock_Golem = Monster('Rock Golem', 300, 2, 0, Fists, 'earth')
# Wind
Vampire = Monster('Vampire', 150, 8, 0, Fists, 'wind')
# Nature
Werewolf = Monster('Werewolf', 150, 8, 0, Axe, 'nature')
# Lightning
Cyclops = Monster('Cyclops', 200, 7, 50, Club, 'lightning')
# Ghost
Reaper = Monster('Reaper', 200, 9, 0, Scythe, 'ghost')
