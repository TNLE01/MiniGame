from Stats import *

axe = Weapon('axe', 1, 2, 3, 4, 5, 1)
le = Earth('le', 100, 50, 200, axe, 300)
le.test()
print(le.weapon.power)
le.name = 'tim'
le.test()
print(le.EP)
time.sleep(3)
print('next')
print(Fists.test())