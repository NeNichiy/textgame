import generate
import main
import unitclass
import random
import itemlist
import copy
def level(num):
    n = (num + 2) * 2
    A = generate.generate(n)
    litemlist = itemlist.mainitemlist

    print('начало генерации')
    tritem1 = random.choice(litemlist)
    print(tritem1)
    litemlist.remove(tritem1)
    print(litemlist)
    tritem2 = random.choice(litemlist)
    print(tritem2)
    litemlist.remove(tritem2)
    s = n // 2
    p = [s, s]
    while True:
        for i in range(n):
            for j in range(n):
                if j == p[0] and i == p[1]:
                    print('p', end=' ')
                else:
                    print(A[i][j], end=' ')
            print()
        inp = input()
        print(p)
        if A[p[1] - 1][p[0]] != '.':
            print('вверх можно')
        else:
            print([p[0], p[1] - 1])
            print(A[p[1] - 1][p[0]])
        if inp == 's' and p[1] < n and A[p[1] + 1][p[0]] != '.':
            p = [p[0], p[1] + 1]
        elif inp == 'a' and p[0] > 0 and A[p[1]][p[0] - 1] != '.':
            p = [p[0] - 1, p[1]]
        elif inp == 'w' and p[1] > 0 and A[p[1] - 1][p[0]] != '.':
            p = [p[0], p[1] - 1]
        elif inp == 'd' and p[0] < n and A[p[1]][p[0] + 1] != '.':
            p = [p[0] + 1, p[1]]
        elif inp == 'end':
            break


        if A[p[1]][p[0]] == '#':
            for i in range(n):
                for j in range(n):
                    if j == p[0] and i == p[1]:
                        print('p', end=' ')
                    else:
                        print(A[i][j], end=' ')
                print()
            unit_list1 = [copy.deepcopy(random.choice(unitclass.unlist)) for i in range(num + 2)]
            main.battle(unit_list1)
            A[p[1]][p[0]] = '[]'



        elif A[p[1]][p[0]] == '$1':
            print(f'Сокровищница!')
            if tritem1.name != 'Предмет взят':
                print(f'{tritem1.name}')
                print(f'{tritem1.script}')
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

#level(4)

