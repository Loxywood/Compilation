#include "automate.h"

unsigned int identificateur(char * str){

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

    //En fonction de l'état on retourne une valeur :
    if (state == 1){
        return 1;
    }
    return 0;
}

unsigned int nbr_entier(char * str){

    unsigned int state = 0;

    for(size_t i =0; i<strlen(str);i++){

        switch(state){

            case 0:
                if((str[i]>=48) && (str[i]<=57)){
                    state = 1;
                }else{
                    state=2;
                }
                break;
            case 1:
                if((str[i]>=48) && (str[i]<=57)){
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
    if(state == 1){
        return 1;
    }
    return 0;
}

unsigned int affectation(char * str){

    unsigned int state = 0;

    for(size_t i =0; i<strlen(str);i++){

        switch(state){

            case 0:
                if(str[i]==61){
                    state = 1;
                }else{
                    state=2;
                }
                break;
            case 1:
                if(str[i]){
                    state=2;
                }
            case 2:
                state = 2;
                break;
        }
    }
    if(state == 1){
        return 1;
    }
    return 0;
}

unsigned int separateur(char * str){
    unsigned int state = 0;

    for(size_t i =0; i<strlen(str);i++){

        switch(state){

            case 0:
                if(str[i]==59 || str[i]==40 || str[i]==41){
                    state = 1;
                }else{
                    state=2;
                }
                break;
            case 1:
                if(str[i]){
                    state=2;
                }
            case 2:
                state = 2;
                break;
        }
    }
    if(state == 1){
        return 1;
    }
    return 0;
}

unsigned int operateur(char * str){
    unsigned int state = 0;

    for(size_t i =0; i<strlen(str);i++){

        switch(state){

            case 0:
                if(str[i]==42 || str[i]==43 || str[i]==45 || str[i]==47){
                    state = 1;
                }else{
                    state=2;
                }
                break;
            case 1:
                if(str[i]){
                    state=2;
                }
            case 2:
                state = 2;
                break;
        }
    }
    if(state == 1){
        return 1;
    }
    return 0;
}
