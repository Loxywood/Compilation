from analyseur_syntaxique import AnalyseurSyntaxique

#On crée un objet analyseur syntaxique qui prend comme paramètre, une pile, une table d'analyse ainsi qu'une chaîne à analyser
analyseur_syntaxique = AnalyseurSyntaxique()

chaine = "main() { id = nombre ; } $"
analyseur_syntaxique.pile.empiler("$")
analyseur_syntaxique.pile.empiler("<programme>")

analyseur_syntaxique.chaine_terminale = chaine.split()     #Chaîne de caractère à analyser
analyseur_syntaxique.analyse(analyseur_syntaxique.chaine_terminale)