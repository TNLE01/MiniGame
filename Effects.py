class Weapon:

  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level):
    self.name = name
    self.power = power
    self.speed = speed
    self.hitrate = hitrate
    self.critrate = critrate
    self.weapon_range = weapon_range
    self.level = level

  def test(self):
    print(self.name)
    print(self.power)
    print(self.speed)
    print(self.hitrate)
    print(self.critrate)
    print(self.weapon_range)
    print(self.level)


class Self_Harm(Weapon):
  # % extra damage to you
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, self_harm, extrarate):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.self_harm = self_harm
    self.extrarate = extrarate


class Poison(Weapon):
  # Double damage
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, poison):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.poison = poison


class Burn(Weapon):
  # % extra damage to enemy
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, burn, extrarate):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.burn = burn
    self.extrarate = extrarate


class Bounce(Weapon):
  # Attack may bounce back and hit enemy again or you doing have damage
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, bounce, extrarate):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.bounce = bounce
    self.extrarate = extrarate


class Bleed(Weapon):
  # Do extra damage
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, bleed, extrarate):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.bleed = bleed
    self.extrarate = extrarate


class Multi_Shot(Weapon):
  # How many extra shots
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, multi_shot):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.muli_shot = multi_shot


class Rage(Weapon):
  # May rage out and attack and damage increase
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, rage):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.rage = rage


class Zap(Weapon):
  # You may attack twice
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, zap):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.zap =zap


class Headshot(Weapon):
  # Do 3X damage
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, headshot):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.headshot = headshot


class Curse(Weapon):
  # Double damage to both
  def __init__(self, name, power, speed, hitrate, critrate, weapon_range, level, curse):
    super().__init__(name, power, speed, hitrate, critrate, weapon_range, level)
    self.curse = curse


# HitRate

chance0 = ['miss', 'miss']
chance10 = ['hit', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss']
chance20 = ['hit', 'miss', 'miss', 'miss', 'miss']
chance30 = ['hit', 'hit', 'hit', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss']
chance40 = ['hit', 'hit', 'miss', 'miss', 'miss']
chance50 = ['hit', 'miss']
chance60 = ['hit', 'hit', 'hit', 'miss', 'miss']
chance70 = ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'miss', 'miss', 'miss']
chance80 = ['hit', 'hit', 'hit', 'hit', 'miss']
chance90 = ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'miss']
chance100 = ['hit', 'hit']
