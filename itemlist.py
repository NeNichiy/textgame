import main

from unitclass import player

class knife_:
    act = False
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
    act = False
    name = 'Доспех'
    script = '+25 к здоровью'
    def additem(a):
        if a == True:
            player.maxhp += 25
            player.hp += 25
            player.plitemlist.append('cuirass')
        else:
            player.maxhp -= 25
            player.hp -= 25
            player.plitemlist.remove('cuirass')
class lol_:
    act = False
    name = 'Доспех'
    script = '+ 25 к здоровью'
    def additem(a):
        if a == True:
            player.maxhp += 25
            player.hp += 25
            player.plitemlist.append('lol')
        else:
            player.hp -= 25
            player.maxhp -= 25
            player.plitemlist.remove('lol')


class bondage_:
    act = False
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            player.hp += 15
            player.maxhp += 15
            player.dmg += 5
            player.plitemlist.append('bondage')
        else:
            player.hp -= 15
            player.maxhp -= 15
            player.dmg -= 5
            player.plitemlist.remove('bondage')
class hollow_:
    act = False
    name = 'Предмет взят'
    script = ''
    def additem(a):
        return

class solevar_:
    name = 'солевар'
    script = 'солеварит'
    act = True
    cd = 4
    mana = 2
    def additem(a):
        return
    def active(self):
        for unit in main.unlist:
            main.magic_attack(unit, 10)



mainitemlist = [solevar_, solevar_, solevar_]#, hollow_, knife_, cuirass_, bondage_]