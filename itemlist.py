import main
import unitclass
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

class wisemysticalstick_:
    name = 'Мудрая мистическая палка'
    script = '+3 к мудрости \n Наносит урон, равный вашей мудрости умноженной на 10'
    act = True
    cd = 6
    mana = 2

    def additem(a):
        if a == 1:
            player.plitemlist.append(wisemysticalstick_)

            unitclass.player.active_item_list.append(wisemysticalstick_)
        else:
            player.plitemlist.remove(wisemysticalstick_)

            unitclass.player.active_item_list.remove(wisemysticalstick_)
        player.int += (3 * a)

    def active(self):
        print('Выберите цель')
        inp = int(input())
        if main.unlist[inp - 1].st:
            main.magic_attack(main.unlist[inp - 1], player.int * 10)
        else:
            print('Этот уже мертв')

class WiseMysticalTree_:
    name = 'Мудрое Мистическое Дерево'
    script = '+ 10 к мудрости \n Способности и предметы больше не требуют маны \n Наносит урон равный вашей мане умноженной на 15'
    act = True
    cd = 5
    mana = 0
    def additem(a):
        if a == 1:
            player.plitemlist.append(WiseMysticalTree_)

            unitclass.player.active_item_list.append(WiseMysticalTree_)
        else:
            player.plitemlist.remove(WiseMysticalTree_)

            unitclass.player.active_item_list.remove(WiseMysticalTree_)
        player.int += (10 * a)

    def active(self):
        print('Выберите цель')
        inp = int(input())
        if main.unlist[inp - 1].st:
            main.magic_attack(main.unlist[inp - 1], player.int * 15)
        else:
            print('Этот уже мертв')
mainitemlist = [wisemysticalstick_, wisemysticalstick_, wisemysticalstick_]# solevar_#, hollow_, knife_, cuirass_, bondage_