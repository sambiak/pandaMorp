from copy import *

class IA():
    def __init__(self, testVictoire, mouvementPossible):
        self.testVictoire = testVictoire
        self.mouvementPossible = mouvementPossible
    def monminimaxamoi(self, tableau,tourBlanc):
        etat= []
        temp = self.mouvementPossible(tableau)
        if temp == []:
            return 0
        for i in temp:
            etat.append(deepcopy(tableau))
            if tourBlanc:
                etat[len(etat)-1] [i//3][i%3] = 10
                if self.testVictoire(etat[len(etat)-1]) != 0:
                    return 1
            else:
                etat[len(etat)-1] [i//3][i%3] = 1
                if self.testVictoire(etat[len(etat)-1]) != 0:

                    return -1
        valeursEtats = []
        for x in etat:
            valeursEtats.append(self.monminimaxamoi(x, not tourBlanc))
        if tourBlanc:
            return max(valeursEtats)
        else:
            return min(valeursEtats)

    def meilleurMouvement(self, tableau, tourBlanc):
        print(tableau)
        temp=self.mouvementPossible(tableau)
        etat=[None for i in range(9)]
        valeurs = [None for i in range(9)]
        valeurajouer = None
        for i in temp:
            etat[i] = deepcopy(tableau)
            if tourBlanc:
                etat[i] [i//3][i%3] = 10
                if self.testVictoire(etat[i]) != 0:
                    valeurajouer = i
            else:
                etat[i] [i//3][i%3] = 1
                if self.testVictoire(etat[i]) != 0:
                    valeurajouer = i
        if valeurajouer == None:
            for i in etat:
                if i is not None:
                    temp2 = self.monminimaxamoi(i, not tourBlanc)
                    valeurs[etat.index(i)] = temp2
        print("fin")
        print(etat)
        print(valeurs)
        print(valeurajouer)
        if valeurajouer == None and tourBlanc:
            valeurajouer = valeurs.index(max(valeurs))
        elif  valeurajouer == None :
            valeurajouer = valeurs.index(min([x for x in valeurs if x != None]))
        return valeurajouer
