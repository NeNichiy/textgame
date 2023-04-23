import random
import unitclass
import itemlist
import copy
pl_dmg = 70
pl_hp = 500
unit1_dmg = 10
unit1 = 50
unit1_name = 'unitname'
class player:
    st = True
    name = 'игрок'
    dmg = 50
    hp = 100
    plitemlist = []






going = True
def attack(unit, dmg):
    unit.hp -= dmg
    if unit.hp <= 0:
        unit.st = False
        print(f'{unit.name} убит')

    else:
        print(f'{unit.name} получил {dmg} урона')


def battle(unit_list):

    total = 0
    going = True
    print('Бой!')
    unit_show(unit_list)
    print('_' * 60)
    while going:
        print('Атаковать         Использовать предметы         Бежать         Осмотреть поле        Осмотреть героя')
        if input() == 'атаковать' or '1':
            print("Номер цели")
            attack(unit_list[int(input())-1], player.dmg)






        unit_attack(unit_list)
        total = 0
        print('Враги на экране:')
#        print(unit_list)
        for unit in unit_list:
            if unit.st == True:
                print(f'{unit.name}, {unit.hp} здоровья')
            else:
                print(f'{unit.name}, мертв')
                total += 1
                if total == len(unit_list):
                    print("Конец боя")
                    going = False


    return
def unit_show(unit_list):
    print(unit_list)
    total = 0
    print('Враги на экране:')
    for unit in unit_list:
        if unit.st == True:
            print(f'{unit.name}, {unit.hp} здоровья')
        else:
            total += 1
            if total == len(unit_list):
                print("Конец боя")
                going = False

    showplayer()


def showplayer():
    print(f'Игрок: {player.hp} здоровья, {player.dmg} урона')


def unit_attack(unit_list):
    for unit in unit_list:
        if unit.st == True:
            attack(player, unit.dmg)
    if player.hp <= 0:
        going = False
        print('Вы погибли')
        print('#######')
        print('########')
        print('#######')
        print('###')
        print('###')
        exit()

