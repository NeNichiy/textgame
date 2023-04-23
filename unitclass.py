class creep:

    st = True
    name = 'Прихвостень'
    dmg = 10
    hp = 30
class kn:
    st = True
    name = 'Воин'
    dmg = 25
    hp = 40
class lol:
    st = True
    name = 'Даунич'
    dmg = 15
    hp = 25

class Unit:
    def __init__(self, name, hp, dmg, st):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.st = st
creep = Unit('Прихвостень', 30, 10, True)
kn = Unit('Воин', 40, 25, True)
lol = Unit('Даунич', 15, 25, True)
unlist = [creep, kn]
