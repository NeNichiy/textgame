import random
import unitclass
import itemlist
import copy








going = True
def attack(unit, dmg):
    mul = 1 - (0.06 * unit.armour) / (1 + (0.06 * unit.armour))
    unit.hp -= int(dmg * mul)
    if unit.hp <= 0:
        unit.st = False
        print(f'{unit.name} убит')

    else:
        print(f'{unit.name} получил {int(dmg * mul)} урона')
def magic_attack(unit, dmg):

    unit.hp -= dmg
    if unit.hp <= 0:
        unit.st = False
        print(f'{unit.name} убит')

    else:
        print(f'{unit.name} получил {dmg} урона')

def battle(unit_list):
    pl_turn = True
    global unlist
    unlist = unit_list
    total = 0
    going = True
    print('Бой!')
    unit_show(unit_list)
    print('_' * 60)
    while going:
        while pl_turn:
            print('Атаковать         Использовать предметы         Бежать')
            inp = input()
            if inp == 'атаковать' or inp == '1':
                if unitclass.player.cur_stamin > 0:
                    print("Номер цели")
                    unitclass.player.cur_stamin -= 1
                    attack(unit_list[int(input())-1], unitclass.player.dmg)
                else:
                    print('У вас недостаточно сил')

            elif inp == 'Бежать' or inp == '3':
                return 'run'


            elif inp == '2':
                for item in unitclass.player.active_item_list:
                    print(item.name, end='     ')
                    print()
                    print('Выберите номер предмета')
                    inp = int(input())
                    unitclass.player.active_item_list[inp - 1].active(1)
            elif inp == '4':
                pl_turn = False




        unit_attack(unit_list)
        pl_turn = True
        unitclass.player.cur_stamin += 1
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
                    return 'won'





def unit_show(unit_list):
 #   print(unit_list)
    total = 0
    print('Враги на экране:')
    for unit in unit_list:
        if unit.st == True:
            if unit.name == 'Игрок:':
                print(f'    {unit.name}, {unit.hp}/{unit.maxhp} здоровья, {unit.cur_stamina}/{unit.stamina} сил')
            print(f'    {unit.name}, {unit.hp} здоровья')
        else:
            total += 1
            if total == len(unit_list):
                print("Конец боя")
                going = False
                return 'won'
    showplayer()


def showplayer():
    print(f'Игрок: {unitclass.player.hp} здоровья, {unitclass.player.dmg} урона')


def unit_attack(unit_list):
    for unit in unit_list:
        if unit.st == True:
            attack(unitclass.player, unit.dmg)
    if unitclass.player.hp <= 0:
        going = False
        print('Вы погибли')
        print('#######')
        print('########')
        print('#######')
        print('###')
        print('###')
        exit()

