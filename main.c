#include "automate.h"

int main (){

    printf("Résultat : %u\n",identificateur("2bonjour"));
    printf("Résultat : %u\n",nbr_entier("147"));
    printf("Résultat : %u\n",affectation("="));
    printf("Résultat : %u\n",separateur(";"));
    printf("Résultat : %u\n",operateur("*"));

    return EXIT_SUCCESS;
}