#S'accorder sur les types des paramètres

VN = ["<programme>",                  #Ensemble des non-terminaux
"<liste_instructions>",
"<instruction>",
"<liste_declarations>",
"<declaration>",
"<type>",
"<affectation>",
"<test>",
"<condition>",
"<operateur>]"]

VT = ["X","<",">","=","id","main()","nombre","if","else","int","float","{","}",";","","$"]

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
    def voir_dernier(self):
        return self.p[-1]

    def afficher_pile(self):
        print(self)

#Les classes Arbre et Noeud nous srerviront pour produire l'arbre de syntaxe
class Arbre :

    def __init__(self,racine=None):
        self.racine = Noeud(racine)

class Noeud :

    def __init__(self,val=None):
        self.valeur = val
        self.enfants = []

    def ajouter_enfant(self, valeur):
        self.enfants.append(Noeud(valeur))


class  AnalyseurSyntaxique :

    def __init__(self):
        self.pile = Pile()
        self.pile.empiler("$")
        self.pile.empiler("<programme>")
        self.chaine_terminale = []
        self.table_analyse = [
        ["X","<",">","=","id","main()","nombre","if","else","int","float","{","}",";","","$"],
        ["<programme>",0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        ["<liste_instruction>",0,0,0,5,0,0,5,0,0,0,0,6,0,0,0],
        ["<instruction>",0,0,0,7,0,0,8,0,0,0,0,0,0,0,0],
        ["<liste_declaration>",0,0,0,3,0,0,3,0,2,2,0,3,0,0,0],
        ["<declaration>",0,0,0,0,0,0,0,0,4,4,0,0,0,0,0],
        ["<type>",0,0,0,0,0,0,0,0,9,10,0,0,0,0,0],
        ["<affectation>",0,0,0,11,0,0,0,0,0,0,0,0,0,0,0],
        ["<test>",0,0,0,0,0,0,12,0,0,0,0,0,0,0,0],
        ["<condition>",0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0],
        ["<operateur>",14,15,16,0,0,0,0,0,0,0,0,0,0,0,0]
        ]

        self.dico_regles = {
            1:"main() { <liste_declarations> <liste_instructions> }",
            2:"<declaration> <liste_declarations>",
            3:"",
            4:"<type> id",
            5:"<instruction> <liste_instructions>",
            6:"",
            7:"<affectation> ",
            8:"<test>",
            9:"int",
            10:"float",
            11:"id = nombre ;",
            12:"if <condition> <instruction> else <instruction> ;",
            13:"id <operateur> nombre",
            14:"<",
            15:">",
            16:"="
        }
        self.arbre_syntaxique = Arbre(Noeud("<programme>"))

    def analyse(self):

        #I est une variable qui nous permettra de parcourir la chaîne à analyser
        i = 0
        noeud_courant = self.arbre_syntaxique.racine

        #Cette boucle while True sera stoppée dans le cas  ou l'analyse réussie, autrement elle va lever des exception.
        while True :

            #On considère x, le sommet de la pile et elt le symbolecourant.
            X = self.pile.voir_dernier()
            elt = self.chaine_terminale[i]
            if noeud_courant.enfants:
                noeud_courant = noeud_courant.enfants[-1]
            else :
                noeud_courant = noeud_courant
            

            #On les affiche.
            print(f"X : {X}, elt : {elt}")

            #Cas 1 : X est un non-terminal :
            if X in VN :


                ligne = VN.index(X)
                colonne = VT.index(elt)
                #Cas 1.1 : Une règle existe dans la table d'analyse pour X et elt. On l'applique.
                if self.dico_regles.get(self.table_analyse[ligne+1][colonne]) is not None :
                    regle = self.dico_regles.get(self.table_analyse[ligne+1][colonne])
                    
                    self.pile.depiler()
                    for y in reversed(regle.split()) :
                        if y != "" :
                            self.pile.empiler(y)
                            noeud_courant.ajouter_enfant(y)
                    print(f"Règle appliquée : {regle}")
                #Cas 1.2 : Aucune règle n'existe. On lève une exception.
                else : 
                    raise Exception("Erreur d'analyse syntaxique : Aucune règle correspondante trouvée.")
                
            #Cas 2 : X est un terminal :
            else :
                #Cas 2.1 : X vaut dollar. Si elt vaut aussi dollar, l'analyse est réussie.
                if X == "$" :
                    if elt == "$" :
                        print("Analyse syntaxique réussie !")
                        return True
                    else :
                        raise Exception("Erreur d'analyse syntaxique : Symbole terminal inattendu.")
                #Cas 2.2 : X != de dollar. On vérifie que elt == X. Si c'est le cas on dépile et on continue.
                elif X in VT : 
                    if X == elt :
                        self.pile.depiler()
                        i += 1
                    else :
                        raise Exception("Erreur d'analyse syntaxique : Symbole terminal attendu mais non trouvé.")
                #Cas 2.3 : X n'est ni dollar ni un terminal. On lève une exception.
                else :
                    raise Exception("Erreur d'analyse syntaxique : Symbole inconnu.")