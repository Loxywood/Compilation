#include "automate.h"

int main (){

    // printf("Nombre identitficateur : %u\n",identificateur("2bonjour"));
    // printf("Nombre entier : %u\n",nbr_entier("147"));
    // printf("Nombre affectation : %u\n",affectation("="));
    // printf("Nombre séparateur : %u\n",separateur(";"));
    // printf("Nombre opérateur : %u\n",operateur("*"));

    printf("Affichage des tokens : \n");
    analyseur_lexical("var1 = 18 + 27");

    return EXIT_SUCCESS;
}