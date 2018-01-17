#include <stdio.h>
#include <string.h>
int main(void){
    // 自分の得意な言語で
    // Let's チャレンジ！！

    char str[1000];
    int paiza[1000];
    fgets(str, sizeof(str), stdin);
    for(int i = 0;i < sizeof(str); i++){
        paiza[i] = 0;
    }
    int j = 0;
    for(int i = 0; i<sizeof(str); i++){
        if(str[i] == '<'){
        paiza[j] = paiza[j] + 10;
        }else if(str[i] == '/'){
        paiza[j] = paiza[j] + 1;
        }else if(str[i] == '+'){
        j++;
        }else{
            break;
        }
    }
    int result = 0;
    for(int i = 0; i<sizeof(str); i++){
        result = result +  paiza[i];
    }
    printf("%d", result);
    return 0;
}
