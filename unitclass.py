
class creep:

    st = True
    name = 'Прихвостень'
    dmg = 10
    hp = 30
class player:
    st = True
    stamin = 1
    cur_stamin = 1
    int = 2
    cur_int = 2
    name = 'игрок'
    dmg = 3000
    maxhp = 1000
    hp = 1000
    armour = 0
    plitemlist = []
    active_item_list = []
    cd_dict = {}







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
    def __init__(self, name, hp, armour, dmg, st, maxhp):
        self.armour = armour
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.st = st
creep = Unit('Прихвостень', 30, 1, 10, True, 30)
kn = Unit('Воин', 40, 3, 25, True, 40)
lol = Unit('Даунич', 15, 0, 25, True, 15)
unlist = [creep, kn]
