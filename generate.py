import random
import itemlist
maplist = ['$', '@', 'X']
tritem1 = '-'
tritem2 = '-'
def generate(n):
#    litemlist = itemlist.mainitemlist
    counter = 1
  #  print('начало генерации')
#   # tritem1 = random.choice(litemlist)
#    print(tritem1)
#    litemlist.remove(tritem1)
#    print(litemlist)
#    tritem2 = random.choice(litemlist)
#    print(tritem2)
#    litemlist.remove(tritem2)
    s = n // 2
    A = [['.' for i in range(n)] for j in range(n)]
    A[s][s] = 'S'
    rooms = [[s, s]]
    l = [[-1, 0], [1, 0], [0, 1], [0, -1]]
#    print(A)
    while counter < (n * 2):
        rv = []
  #      print('new cicle')
        new_room_pool = []
        for basedroom in rooms:
            if [basedroom[0] + 1,  basedroom[1]] not in rooms and basedroom[0] + 1 < len(A):
  #              print('up')
                new_room_pool.append([basedroom[0] + 1,  basedroom[1]])
            if [basedroom[0] - 1,  basedroom[1]] not in rooms and basedroom[0] - 1 >= 0:
                new_room_pool.append([basedroom[0] - 1,  basedroom[1]])
 #               print('down')
            if [basedroom[0],  basedroom[1] + 1] not in rooms and basedroom[1] + 1 < len(A[0]):
                new_room_pool.append([basedroom[0],  basedroom[1] + 1])
 #               print('right')
            if [basedroom[0],  basedroom[1] - 1] not in rooms and basedroom[1] - 1 >= 0:
                new_room_pool.append([basedroom[0], basedroom[1] - 1])
#                print('left')
#        print(new_room_pool)
        for r in new_room_pool:
            c = new_room_pool.count(r)
            if c > 1:
                for i in range(c):
                    new_room_pool.remove(r)




        newroom = random.choice(new_room_pool)



#        print(len(A))
#        print(newroom)
        rooms.append(newroom)
        A[newroom[0]][newroom[1]] = '#'
#                for i in range(n):
#                   for j in range(n):
#                        print(A[i][j], end=' ')
#                    print( )

        counter += 1
        continue


    lrooms = rooms
    lrooms.remove([s,s])
    tresroom1 = random.choice(lrooms)
    lrooms.remove(tresroom1)

    bt = 0
    bti = tresroom1
    A[bti[0]][bti[1]] = '$1'

    for r in lrooms:
        ct = (((abs(int(r[0]) - tresroom1[0])) ** 2) + (int(abs(r[1] - tresroom1[1]) ** 2))) ** (1/2)

        if ct > bt:

            bt = ct
            bti = r
    A[bti[0]][bti[1]] = '$2'
    lrooms.remove(bti)

    br = 0
    bri = [s, s]
    for r in lrooms:


        cr = (((abs(int(r[0]) - s)) ** 2) + (int(abs(r[1] - s) ** 2))) ** (1/2)
#        print(cr, r)
        if cr > br:
#            print('yees')
            br = cr
            bri = r
    A[bri[0]][bri[1]] = 'X'
    lrooms.remove(bri)
    room_craft = random.choice(lrooms)
    A[room_craft[0]][room_craft[1]] = '%'

#    print('конец', bri)
#    print(itemlist.mainitemlist)
    return A
#print('m')
m = generate(5)
#for i in range(5):
#    for j in range(5):
#        print(m[i][j], end=' ')
#    print()

#comment