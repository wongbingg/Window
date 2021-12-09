#include <stdio.h>

//함수선언
int rect(int a,int b,int c);


int main(){

    int a = 50;
    int b = 20;
    int c = 10;

    printf("%d",rect(a,b,c));
    return 0;
}

//함수정의
int rect(int a,int b,int c){

    return a*b*c;
}
