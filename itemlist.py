import main
from unitclass import player

class knife_:
    name = 'Нож'
    script = '+10 к урону'
    def additem(a):
        if a == True:
            player.dmg += 10
            player.plitemlist.append('knife')
        else:
            player.dmg -= 10
            player.plitemlist.remove('knife')
class cuirass_:
    name = 'Доспех'
    script = '+25 к здоровью'
    def additem(a):
        if a == True:
            player.hp += 25
            player.plitemlist.append('cuirass')
        else:
            player.hp -= 25
            player.plitemlist.remove('cuirass')
class lol_:
    name = 'Доспех'
    script = '+ 25 к здоровью'
    def additem(a):
        if a == True:
            player.hp += 25
            player.plitemlist.append('lol')
        else:
            player.hp -= 25
            player.plitemlist.remove('lol')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            player.hp += 15
            player.dmg += 5
            player.plitemlist.append('bondage')
        else:
            player.hp -= 15
            player.dmg -= 5
            player.plitemlist.remove('bondage')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            player.hp += 15
            player.dmg += 5
            player.plitemlist.append('bondage')
        else:
            player.hp -= 15
            player.dmg -= 5
            player.plitemlist.remove('bondage')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            player.hp += 15
            player.dmg += 5
            player.plitemlist.append('bondage')
        else:
            player.hp -= 15
            player.dmg -= 5
            player.plitemlist.remove('bondage')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            player.hp += 15
            player.dmg += 5
            player.plitemlist.append('bondage')
        else:
            player.hp -= 15
            player.dmg -= 5
            player.plitemlist.remove('bondage')
class hollow_:
    name = 'Предмет взят'
    script = ''
    def additem(a):
        return


mainitemlist = [knife_, cuirass_, lol_, bondage_]