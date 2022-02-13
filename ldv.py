#! /usr/bin/python3

from math import gcd

def isObstacle(map, pos):
    return (map[pos[0]][pos[1]]==1)

def trajNaive(coordA, coordB):
    def sign(i):
        return -1 if i<0 else 1
    coorA = (coordA[0]+0.5, coordA[1]+0.5)
    coorB = (coordB[0]+0.5, coordB[1]+0.5)
    dX = coordB[0] - coordA[0]
    dY = coordB[1] - coordA[1]
    ltrav=[]
    if dX != 0:
        sig = sign(dX)
        for i in range(coordA[0]+sig, coordB[0]+sig, sig):
            # y pour x = i
            j = coorA[1] + (dY/dX)*(i-coorA[0])
            # print("x : (%s, %s)" % (i,j))
            if int(j)!=j:
                ltrav.append((i,int(j)))
                ltrav.append((i-sig,int(j)))
    if dY != 0:
        sig = sign(dY)
        for j in range(coordA[1]+sig, coordB[1]+sig, sig):
            # x pour y = j
            i = coorA[0] + (dX/dY)*(j-coorA[1])
            # print("y : (%s, %s)" % (i,j))
            if int(i)!=i:
                ltrav.append((int(i),j))
                ltrav.append((int(i),j-sig))
    unique=[]
    for e in ltrav:
        if e!= coordA and e!=coordB and not e in unique:
            unique.append(e)
    # not efficient, by the way
    return unique

def traj(coordA, coordB):
    print("LDV2 : (%s,%s)->(%s,%s)" % (coordA[0],coordA[1],coordB[0],coordB[1]))
    def sign(i):
        return -1 if i<0 else 1
    def seq(dX,dY):
        a = gcd(dX,dY)
        if a > 1:
            bar = seq(dX//a, dY//a) # for int type, is actual division
            res = [a*bar[0], a*bar[1]]
            return res
        if (dX%2)==(dY%2)==1:
            bar = seq(dX//2, dY//2)
            res = [bar[0]+[dX%2]+bar[0], bar[1]+[dY%2]+bar[1]]
            return res
        elif (dY>1 and (dX%2)==1) or (dX>1 and (dY%2)==1):
            bar = seq(dX//2, dY//2) # one division is without remainder
            res = [bar[0]+[dX%2]+bar[0], bar[1]+[dY%2]+bar[1]]
            return res
        elif dX>dY:
            return [[(i+1)%2 for i in range(dX+dY)], [i%2 for i in range(dX+dY)]]
        return [[i%2 for i in range(dX+dY)], [(i+1)%2 for i in range(dX+dY)]]
    x=coordA[0]
    y=coordA[1]
    dX = coordB[0] - coordA[0]
    signX = sign(dX)
    dY = coordB[1] - coordA[1]
    signY = sign(dY)
    sequenceX,sequenceY = seq(abs(dX),abs(dY))
    # print("starting", x,y,"Sequences :",sequenceX,sequenceY)
    l=len(sequenceX)
    cells=[]
    for i in range(l)
        x += signX*sequenceX[i]
        y += signY*sequenceY[i]
        # print("(%s,%s)" % (x,y), end="  ")
        cells.append((x,y))
    return cells[:-1] # cut the last one

def LOS(map,a,b):
    for pos in traj(a,b):
        if isObstacle(pos):
            return False
    return True




# Exemple de map, pas vraiment utile si on ne met pas des obstacles à la main
map = [[0 for i in range(10)] for j in range(10)]




target =(1,8)

print(trajNaive((0,0), target))


print(traj((0,0), target))











# ..
