import main

class knife_:
    name = 'Нож'
    script = '+10 к урону'
    def additem(a):
        if a == True:
            main.player.dmg += 10
            main.player.plitemlist.append('knife')
        else:
            main.player.dmg -= 10
            main.player.plitemlist.remove('knife')
class cuirass_:
    name = 'Доспех'
    script = '+25 к здоровью'
    def additem(a):
        if a == True:
            main.player.hp += 25
            main.player.plitemlist.append('cuirass')
        else:
            main.player.hp -= 25
            main.player.plitemlist.remove('cuirass')
class lol_:
    name = 'Доспех'
    script = '+ 25 к здоровью'
    def additem(a):
        if a == True:
            main.player.hp += 25
            main.player.plitemlist.append('lol')
        else:
            main.player.hp -= 25
            main.player.plitemlist.remove('lol')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            main.player.hp += 15
            main.player.dmg += 5
            main.player.plitemlist.append('bondage')
        else:
            main.player.hp -= 15
            main.player.dmg -= 5
            main.player.plitemlist.remove('bondage')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            main.player.hp += 15
            main.player.dmg += 5
            main.player.plitemlist.append('bondage')
        else:
            main.player.hp -= 15
            main.player.dmg -= 5
            main.player.plitemlist.remove('bondage')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            main.player.hp += 15
            main.player.dmg += 5
            main.player.plitemlist.append('bondage')
        else:
            main.player.hp -= 15
            main.player.dmg -= 5
            main.player.plitemlist.remove('bondage')
class bondage_:
    name = 'Бондаж'
    script = '+15 к здоровью, +5 к урону'
    def additem(a):
        if a == True:
            main.player.hp += 15
            main.player.dmg += 5
            main.player.plitemlist.append('bondage')
        else:
            main.player.hp -= 15
            main.player.dmg -= 5
            main.player.plitemlist.remove('bondage')
class hollow_:
    name = 'Предмет взят'
    script = ''
    def additem(a):
        return


mainitemlist = [knife_, cuirass_, lol_, bondage_]