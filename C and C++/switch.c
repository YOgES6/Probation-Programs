#include<stdio.h>
int main()
{
char s;
int a;
printf("Enter a number(1 or 2 or 3): ");
scanf("%d",&a);

switch(a)
{
case 1:s='O';
break;
case 2:s='T';
break;
case 3:s='R';
break;
default:printf("SOmething wrong");
break;
}
printf("\n\n %c",s);
}
