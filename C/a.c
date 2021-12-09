#include<stdio.h>

int sec_power(int a);

int main(){

	int a,b;

	printf("1~20 사이의 정수를 입력하세요: ");
	scanf("%d",&a);

	if(a>=1 && a<=20){
		printf("%d\n",sec_power(a));

	}else{
		printf("제곱값의 범위를 잘못입력하셨습니다.\n");

	}
	return 0;

}

//함수정의
int sec_power(int a){
	if(a==0)
		return 1;

	return 2*sec_power(a-1);
}