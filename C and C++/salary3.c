#include<stdio.h>
int main()
{ 
int a[20],b[20],c,d,sw=10000,l,m;
float p1,p2,g;
char s[][30]={"January","February","March","April","May","June","July","August","September","October","November","December"};


for(int i=0; i<12; i++)
{
printf("\nNo.of.Worked Saturdays in %s: ",s[i]);
scanf("%d",&a[i]);
c=a[i]+c;
}
printf("\n\nTotal of worked saturdays: %d",c);


for(int k=0; k<12; k++)
{
printf("\nNo.of.Half Saturdays in %s: ",s[k]);
scanf("%d",&b[k]);
d=b[k]+d;
}
printf("\n\nTotal of worked saturdays: %d",d);


l=c*1;
m=d*2;
p1=(l*sw)/100;
p2=(m*sw)/100;
g=p1+p2+sw;
printf("\n\nYearly Bonus: %.1f",p1+p2);
printf("\nYour monthly salary: %d",sw);
printf("\nTotal salary amount(December) with bouns: %.1f",g);
}
