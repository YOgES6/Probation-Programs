#include<stdio.h>
int main()
{
int m,s,day,h,l=100,e,g;
printf("\n\nEnter the number of days worked: ");
scanf("%d",&day);
printf("\n   Enter the total hours worked: ");
scanf("%d",&h);
m=day*24;
if(h<=8)
{
    printf("!!!You worked less than 8 hours");
    main();
}
s=h-8;
  if(s<=m)
   {
   for(int i=s; i==0; i-4)
   {
       
       e=100+l;
     
   }
   g=e+8000;
   printf("Salary: %d",g);
   }
   printf("\n\n%d  ",s);
}               
