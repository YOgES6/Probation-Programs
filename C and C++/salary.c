#include<stdio.h>
int main()
{
    int ot,a,s,z,q,sw,d;
    char l[30],m[30],y[10],g[10];
    printf("OT(In hours): ");
    scanf("%d",&ot);
    printf("\n1.Single OT\n 2.double OT: ");
    scanf("%d",&a);
    if(a==1)
    {
        s=ot*100;
        printf("Over time salary of month March: %d",s);
    }
    else if(a==2)
    {
        printf("Enter timing daywise:  ");
        for(int i=0; i<=6; i++)
        {
            scanf("%c",&l[i]);
        g[i]=l[i]-4;
        for(int j=0; j<=6; j++)
        {
            m[j]=l[i];
            }
        
        for(int j=0; j<=6; j++)
        {
        switch (m[j]) 
        {
        case '5': y[1]=1;
        break;
        case '6': y[2]=2;
        break;
        case '7': y[3]=3;
        break;
        case '8': y[4]=4;
        break;
        }
        for(int f=1; f<=4; f++)
        {
        z=y[f]+0;
        }
        d=z*20;
        q=g[i]*10;
        }
        
        }sw=d+q;
        printf("Over time salary of month March: %d",sw);
    }
        
}
