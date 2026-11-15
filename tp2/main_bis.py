import analyseur_syntaxique

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

#On crée un objet analyseur syntaxique qui prend comme paramètre, une pile, une table d'analyse ainsi qu'une chaîne à analyser
analyseur_syntaxique = analyseur_syntaxique.AnalyseurSyntaxique()

dico_regles = {
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
#Le symbole vide ne se traduit pas nécésairrement par la chaîne vide, garder ça en tête en cas d'erreur
table_analyse_test = [
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

def analyse(chaine):

    i = 0

    while True :

        X = analyseur_syntaxique.pile.voir_dernier()
        elt = analyseur_syntaxique.chaine_terminale[i]

        print(f"X : {X}, elt : {elt}")

        if X in VN :

            ligne = VN.index(X)
            colonne = VT.index(elt)

            if dico_regles.get(analyseur_syntaxique.table_analyse[ligne+1][colonne]) is not None :
                regle = dico_regles.get(analyseur_syntaxique.table_analyse[ligne+1][colonne])
                
                analyseur_syntaxique.pile.depiler()
                for y in reversed(regle.split()) :
                    if y != "" :
                        analyseur_syntaxique.pile.empiler(y)
                print(f"Règle appliquée : {regle}")

            else : 
                raise Exception("Erreur d'analyse syntaxique : Aucune règle correspondante trouvée.")
                return False
        else :
            if X == "$" :
                if elt == "$" :
                    print("Analyse syntaxique réussie !")
                    return True
                else :
                    raise Exception("Erreur d'analyse syntaxique : Symbole terminal inattendu.")
                    return False
            elif X in VT : 
                if X == elt :
                    analyseur_syntaxique.pile.depiler()
                    i += 1
                else :
                    raise Exception("Erreur d'analyse syntaxique : Symbole terminal attendu mais non trouvé.")
                    return False
            else :
                raise Exception("Erreur d'analyse syntaxique : Symbole inconnu.")


chaine = "main() { id = nombre ; } $"
analyseur_syntaxique.pile.empiler("$")
analyseur_syntaxique.pile.empiler("<programme>")

analyseur_syntaxique.chaine_terminale = chaine.split()
analyseur_syntaxique.table_analyse = table_analyse_test     #Chaîne de caractère à analyser
analyse(chaine)