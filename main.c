#include "automate.h"

int main (){

    printf("Résultat : %u\n",identificateur("2bonjour"));
    printf("Résultat : %u\n",nbr_entier("147"));
    printf("Résultat : %u\n",affectation("="));
    printf("Résultat : %u\n",separateur(";"));
    printf("Résultat : %u\n",operateur("*"));

    printf("Affichage des tokens : \n");
    analyseur_lexical("var1 = 1,8 + 27");

    return EXIT_SUCCESS;
}