import generate
import main
import unitclass
import random
import itemlist
import copy
import craftRecipes
knownrooms = []
def level(num):
    roomdict = {}
    n = (num + 2) * 2
    A = generate.generate(n)
    litemlist = itemlist.mainitemlist

  #  print('начало генерации')
    tritem1 = random.choice(litemlist)
 #   print(tritem1)
    litemlist.remove(tritem1)
#    print(litemlist)
    tritem2 = random.choice(litemlist)
#    print(tritem2)
    litemlist.remove(tritem2)
    s = n // 2
    p = [s, s]
    if [p[0], p[1] + 1] not in knownrooms:
        knownrooms.append([p[0], p[1] + 1])
    if [p[0], p[1] - 1] not in knownrooms:
        knownrooms.append([p[0], p[1] - 1])
    if [p[0] + 1, p[1]] not in knownrooms:
        knownrooms.append([p[0] + 1, p[1]])
    if [p[0] - 1, p[1]] not in knownrooms:
        knownrooms.append([p[0] - 1, p[1]])

    while True:
        for i in range(n):
            for j in range(n):
                if j == p[0] and i == p[1]:
                    print('p', end=' ')
                elif [j, i] in knownrooms:

                    print(A[i][j], end=' ')
                else:
                    print('.', end=' ')
            print()
        print()


        inp = input()
#        print(p)


        lr = p
        if inp == 's' and p[1]+1 < n and A[p[1] + 1][p[0]] != '.':
            p = [p[0], p[1] + 1]
        elif inp == 'a' and p[0] > 0 and A[p[1]][p[0] - 1] != '.':
            p = [p[0] - 1, p[1]]
        elif inp == 'w' and p[1] > 0 and A[p[1] - 1][p[0]] != '.':
            p = [p[0], p[1] - 1]
        elif inp == 'd' and p[0]+1 < n and A[p[1]][p[0] + 1] != '.':
            p = [p[0] + 1, p[1]]
        elif inp == 'end':
            break
#        print('player', p)
        if [p[0], p[1] + 1] not in knownrooms:
            knownrooms.append([p[0], p[1] + 1])
        if [p[0], p[1] - 1] not in knownrooms and p[1] >= 1:
            knownrooms.append([p[0], p[1] - 1])
        if [p[0] + 1, p[1]] not in knownrooms:
            knownrooms.append([p[0] + 1, p[1]])
        if [p[0] - 1, p[1]] not in knownrooms and p[0] - 1 >= 0:
            knownrooms.append([p[0] - 1, p[1]])
#        print(knownrooms)

        for i in range(n):
            for j in range(n):
                if A[i][j] == '#':
                    roomdict[(i, j)] = [copy.deepcopy(random.choice(unitclass.unlist)) for i in range(num + 2)]
 #                   print(roomdict.items())
                elif [j, i] in knownrooms:

                    print(A[i][j], end=' ')
                else:
                    print('.', end=' ')
            print()
        print()







        if A[p[1]][p[0]] == '#':

 #           print(roomdict[(p[1], p[0])])
            res = main.battle(roomdict[(p[1], p[0])])
#            print(res)
            if res == 'won':
                A[p[1]][p[0]] = '[]'
                print('Победа!')
            elif res == 'run':
                p = lr



        elif A[p[1]][p[0]] == '$1':
            print(f'Сокровищница!')
            if tritem1.name != 'Предмет взят':
                print(f'{tritem1.name}')
                print(f'Описание: {tritem1.script}')
                print('Взять?')
                ans = input()
                if ans == '1':
                    tritem1.additem(1)

                    tritem1 = itemlist.hollow_
                else:
                    continue
            else:
                print('Предмет взят')



        elif A[p[1]][p[0]] == '$2':
            print(f'Сокровищница!')
            if tritem2.name != 'Предмет взят':
                print(f'{tritem2.name}')
                print(f'{tritem2.script}')
                print('Взять?')
                ans = input()
                if bool(ans):
                    tritem2.additem(1)

                    tritem2 = itemlist.hollow_
        elif A[p[1]][p[0]] == 'X':
            print('Закончить уровень?')
            ans = input()
            if ans == 'Да':
                return




        elif A[p[1]][p[0]] == '%':
            flag = False
            can_make = []
            print('Начать создание?')
            if input() == 'Да':
                print('Доступные предметы')
                for i in craftRecipes.craftRec.keys():
                    print(i)
                    print(craftRecipes.craftRec[i])
                    craftFlag = True
                    for k in craftRecipes.craftRec[i]:
                        if k not in unitclass.player.plitemlist:
                            craftFlag = False
                    if craftFlag:
                        flag = True
                        can_make.append(i)
                        print(i.name)
                        print(i.script)
                        print('Рецепт:')
                        for rec in craftRecipes.craftRec[i]:
                            print(rec.name)
                    if flag:
                        print('Выберите предмет')
                        inp = int(input())
                        for rec in craftRecipes.craftRec[can_make[inp - 1]]:
                            rec.additem(-1)
                        can_make[inp-1].additem(1)
                        print(f'Создано: {can_make[inp-1].name}')




#level(4)

