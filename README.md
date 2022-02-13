# Ligne de vue

## Algo naïf

Fonctionnement décrit sur le forum, calcul des intersection et ajout des cellules concernées.

**Cellules en plusieurs exemplaires + dans le désordre**

## Fonctionnement de l'algo un peu opti

Pseudo-code
```
cellulesÀTester(pointA, pointB){
    dX = pointB[x] - pointA[x]
    dY = pointB[y] - pointA[y]
    # On calcule les séquences d'incréments (0 ou 1 à chaque étape)
    (séquenceX, séquenceY) = séquences(dX,dY)
    x = pointA[x]
    y = pointA[y]
    signX = 1 si dX >=0 sinon -1
    signY = 1 si dY >=0 sinon -1
    Pour i de 1 à longueur(séquenceX){
        # On se déplace de 1 ou 0 cases, dans le "bon" sens (A->B)
        x = x + signX*séquenceX[i]
        y = y + signY*séquenceY[i]
        Ajouter (x,y) à la liste des cellulesÀTester
    }
    retourner la liste des cellulesÀTester
    # (à l'exception de la dernière, qui est le pointB, donc on peut l'exclure)
}

# Définition des séquences
séquences(dX,dY){
    si pgcd(dX,dY) > 1:
        # Ils ne sont pas premiers entre eux, donc
        # la séquence revient à répéter k pgcd fois
        # une sous-séquence, on récurse !
        foo = séquences(dX/pgcd(dX,dY), dY/pgcd(dX,dY))
        résultat = (répéter(foo[0], pgcd fois), répéter(foo[1], pgcd fois))
        retourner résultat
    sinon si dX et dY impairs:
        # x : [seq(x//2) 1 seq(x//2)]
        # y : [seq(y//2) 1 seq(y//2)]
        foo = séquences(dX//2, dY//2) # division euclidienne
        résultat = (foo[0]+[1]+foo[0], foo[1]+[1]+foo[1])
    sinon si l'un est impair et l'autre plus grand que 1 (donc non nul):
        # x : [seq(x//2) (1 si pair, 0 sinon) seq(x//2)]
        # y : [seq(y//2) (1 si pair, 0 sinon) seq(y//2)]
        foo = séquences(dX//2, dY//2) # division euclidienne
        résultat = (foo[0]+[resteDivision(dX/2)]+foo[0], foo[1]+[resteDivision(dY/2)]+foo[1])
        retourner résultat
    sinon si dX>dY:
        # Alternance en commençant par la direction qui va le + loin
        retourner ([1 0 1 0 1 0 1 ...], [0 1 0 1 0 1 0 ...]) (longueur dX+dY pour chaque séquence)
    sinon :
        # Alternance en commençant par la direction qui va le + loin
        retourner ([ 0 1 0 1 0 1 0 ...], [1 0 1 0 1 0 1 ...]) (longueur dX+dY pour chaque séquence)
}

#LDV
LDV(pointA, pointB, fonctionDetectionObstacle){
    pour case dans cellulesÀTester(pointA, pointB):
        si fonctionDetectionObstacle(case):
            retourner "pas de ldv"
    retourner "il y a une ldv"
}
```

Ainsi la liste des cellules est retournée dans l'ordre de la plus proche à la plus lointaine, avec unicité des cellules dans la liste, pour faciliter les tests.
