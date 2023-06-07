#include<stdio.h>

int main()
{
FILE *ptr;
ptr=fopen("file.dat","w");
char * s;
printf("Enter a text: ");
scanf("%s",&s);
fprintf(ptr,"%s",s);
printf("Done well...");
}

