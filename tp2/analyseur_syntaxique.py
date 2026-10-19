#Il faut renseigner la table d'analyse
#S'accorder sur les types des paramètres

#La classe Pile sert pour définir la Pile
class Pile :

    def __init__(self):
        self.p = []

    def est_vide(self):
        return self.p == []

    def empiler(self,valeur):
        self.p.append(valeur)

    def depiler(self):
        self.p.pop()
    def voir_premier(self):
        return self.p[-1]

#Les classes Arbre et Noeud nous srerviront pour produire l'arbre de syntaxe
class Arbre :

    def __init__(self):
        self.racine = None

class Noeud :

    def __init__(self):
        self.valeur = self.valeur
        self.fils_droit = None
        self.fils_gauche = None 

class  AnalyseurSyntaxique :

    def __init__(self):
        self.pile = Pile()
        self.chaine_terminale = []
        self.table_analyse = [] #Tableau à 2 dimensions qui accueuillera les règles de grammaires

    def analyse(self) :
        while not self.pile.est_vide() :
            x = self.pile.depiler()

