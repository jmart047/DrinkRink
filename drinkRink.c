// Nicco Narbutas

#include <stdio.h>
#include <stdlib.h>

int main(){

char *ingredient;
int usrinput;


while(1){
	printf("Press 1 if you want to enter an ingredient, if not press 2: ");
	scanf("%d", &usrinput);
	if (usrinput == 1){
		printf("Enter an ingredient: ");
		scanf("%s", &ingredient);
		printf("\nyou entered %s\n\n", &ingredient);
		}
	else if (usrinput == 2){
		break;
		}
	else {
		printf("\nYou entered an invalid number!!!\n\n");
		}
}

return 0;

}
