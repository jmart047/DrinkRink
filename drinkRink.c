// Nicco Narbutas

#include <stdio.h>
#include <stdlib.h>

int main(){

char *ingredient;
int usrinput;

printf("Press 1 if you want to enter an ingredient, if not press 2: ");
scanf("%d", &usrinput);


if (usrinput == 1){
	printf("Enter an ingredient: ");
	scanf("%s", &ingredient);
	printf("\nyou entered %s\n\n", &ingredient);
}












return 0;

}
