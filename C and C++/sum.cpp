#include<stdio.h>
#include<stdlib.h>
int main()
{
int x, y;
printf("Enter two number: ");
scanf("%d %d",&x,&y);
printf("%d\n", x-(-y));
printf("%d\n", -(-x-y));
printf("%d\n", abs(-x-y));
printf("%d", x-(~y)-1);
return 0;
}

