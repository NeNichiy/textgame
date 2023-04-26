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
            print('Атаковать         Использовать предметы         Бежать       Закончить ход')
            inp = input()
            if inp == 'атаковать' or inp == '1':
                if unitclass.player.cur_stamin > 0:
                    print("Номер цели")
                    inp = int(input())
                    if unit_list[inp-1].st:
                        unitclass.player.cur_stamin -= 1
                        attack(unit_list[inp-1], unitclass.player.dmg)
                    else:
                        print('Этот уже мертв')
                    showplayer()
                else:
                    print('У вас недостаточно сил')

            elif inp == 'Бежать' or inp == '3':
                return 'run'


            elif inp == '2':
                if len(unitclass.player.active_item_list) != 0:
                    for item in unitclass.player.active_item_list:
                        print(item.name,'(', unitclass.player.cd_dict.get(item, 'готов'), ')', end='     ')
                        print()
                        print('Выберите номер предмета')
                        inp = int(input())
                        if inp <= len(unitclass.player.active_item_list):
                            if unitclass.player.cd_dict.get(unitclass.player.active_item_list[inp - 1], 'готов') == 'готов':
                                if unitclass.player.active_item_list[inp-1].mana <= unitclass.player.cur_int:
                                    unitclass.player.cur_int -= unitclass.player.active_item_list[inp-1].mana
                                    unitclass.player.active_item_list[inp - 1].active(1)
                                    unitclass.player.cd_dict[unitclass.player.active_item_list[inp - 1]] = unitclass.player.active_item_list[inp - 1].cd
                                else:
                                    print('недостаточно мудрости')
                            else:
                                print('предмет на перезарядке')
                        else:
                            print('Такого предмета нет')
                        showplayer()
                else:
                    print('У вас нет предметов')
            elif inp == '4':
                pl_turn = False
                for k in unitclass.player.cd_dict.keys():
                    if unitclass.player.cd_dict[k] != 'готов':
                        if unitclass.player.cd_dict[k] != 1:
                            unitclass.player.cd_dict[k] -= 1
                        else:
                            unitclass.player.cd_dict[k] = 'готов'




        unit_attack(unit_list)
        pl_turn = True
        if unitclass.player.cur_stamin < unitclass.player.stamin:
            unitclass.player.cur_stamin += 1
        if unitclass.player.cur_int < unitclass.player.int:
            unitclass.player.cur_int += 1
        total = 0
        print('Враги на экране:')
#        print(unit_list)
        for unit in unit_list:
            if unit.st == True:
                print(f'    {unit.name}, {unit.hp} здоровья')
            else:
                print(f'    {unit.name}, мертв')
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
            print(f'    {unit.name}, {unit.hp} здоровья')
        else:
            print(f'    {unit.name}, мертв')
            total += 1
            if total == len(unit_list):
                print("Конец боя")
                going = False
                return 'won'
    showplayer()


def showplayer():
    print(f'Игрок: {unitclass.player.hp}/{unitclass.player.maxhp} здоровья, {unitclass.player.dmg} урона, {unitclass.player.cur_stamin}/{unitclass.player.stamin} выносливости')
    print(f'{unitclass.player.cur_stamin}/{unitclass.player.stamin} выносливости, {unitclass.player.cur_int}/{unitclass.player.int} мудрости')

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

