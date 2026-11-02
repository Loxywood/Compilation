import analyseur_syntaxique

chaine = "main() { id = nombre } $"     #Chaîne de caractère à analyser

VN = ["<programme>",                  #Ensemble des non-terminaux
"<liste_instruction>",
"<instruction>",
"<liste_declaration>",
"<declaration>",
"<type>",
"<affectation>",
"<test>",
"<condition>",
"<operateur>]"]

VT = ["X","<",">","=","id","main()","nombre","if","else","int","float","{","}",";",""]

#On crée un objet analyseur syntaxique qui prend comme paramètre, une pile, une table d'analyse ainsi qu'une chaîne à analyser
analyseur_syntaxique = analyseur_syntaxique.AnalyseurSyntaxique()

dico_regles = {
    1:"main() { <liste_declarations> <liste_instructions> }",
    2:"<une_declaration> <liste_declarations>",
    3:"",
    4:"<type> id",
    5:"<une_instruction> <liste_instructions>",
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
#Le symbole vide ne se traduit pas nécésairrement par la chaîne vide, garder ça en tête en cas d'erreur
talbe_analyse_test = [
VT,
["<programme>",0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
["<liste_instruction>",0,0,0,5,0,0,5,0,0,0,0,6,0,0],
["<instruction>",0,0,0,7,0,0,8,0,0,0,0,0,0,0],
["<liste_declaration>",0,0,0,3,0,0,3,0,2,2,0,3,0,0],
["<declaration>",0,0,0,0,0,0,0,0,4,4,0,0,0,0],
["<type>",0,0,0,0,0,0,0,0,9,10,0,0,0,0],
["<affectation>",0,0,0,11,0,0,0,0,0,0,0,0,0,0],
["<test>",0,0,0,0,0,0,12,0,0,0,0,0,0,0],
["<condition>",0,0,0,13,0,0,0,0,0,0,0,0,0,0,0],
["<operateur>",14,15,16,0,0,0,0,0,0,0,0,0,0,0]
]
analyseur_syntaxique.pile.empiler("$")
analyseur_syntaxique.pile.empiler("<programme>")

analyseur_syntaxique.chaine_terminale = chaine.split(" ")
analyseur_syntaxique.table_analyse = talbe_analyse_test

def analyse():

    erreur = False
    accepte = False

    for _ in range(1) :
        print("test")
        x = analyseur_syntaxique.pile.voir_dernier()
        for elt in analyseur_syntaxique.chaine_terminale:

            #On s'occupe de voir si X et elt appartiennent bien à leurs ensemble respectifs
            if (x in VN) and (elt in VT):

                ligne = VN.index(x)
                colonne = VT.index(elt)

                #On retrouve la règle dans la TA.
                regle = (dico_regles.get(talbe_analyse_test[ligne +1 ][colonne])).split(" ")
                print(f"La règle correspondant est : {regle}")

                if regle is not None :
                    analyseur_syntaxique.pile.depiler()
                    for i in range(len(regle),0,-1) :
                        print(regle[i-1])
                        analyseur_syntaxique.pile.empiler(regle[i-1])

            else :
                if x == "$" :
                    if elt == "$" :
                        accepte = True
                    else : 
                        erreur = True
                elif (x in VT) :
                    analyseur_syntaxique.pile.depiler()
                else :
                    erreur = True

analyse()