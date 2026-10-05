#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned int reconnaitre_identificateur(char * str){

    unsigned int state = 0;                             //On définit un état.

    for(size_t i=0; i<strlen(str); i++){                   //Pour chaque caractère de la chaîne :
        switch (state){                                  
            case 0:
                if (str[i] > 97 && str[i] < 122){         //On vérifie que le caractère est bien une minuscule
                    state = 1;
                } else {
                    state = 2;
                }
                break;
            case 1:
                if(((str[i] >= 97) && (str[i] <= 122))||((str[i]>=65) && (str[i] <= 90))||((str[i]>=48)&&(str[i]<=57))){
                    state = 1;
                } else {
                    state = 2;
                }
                break;
            case 2:
                state = 2;
                break;
        }
    }

    //En fonction de 'état on retourne une valeur :
    if (state == 1){
        return 1;
    }
    return 0;
}

int main (){

    printf("Résultat : %u",reconnaitre_identificateur("2bonjour"));

    return EXIT_SUCCESS;
}