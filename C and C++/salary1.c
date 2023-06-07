#include<stdio.h>
int main()
{
    int ot,a,s,q,z,sw,d;
    int l[10],y[10];
    printf("OT(In hours): ");
    scanf("%d",&ot);
    printf("\n1.Single OT\n2.double OT: ");
    scanf("%d",&a);
    if(a==1)
    {
        s=ot*100;
        printf("Over time salary of month March: %d",s);
    }
    else if(a==2)
    {
        printf("Enter timing daywise:  ");
        for(int i=0; i<=4; i++)
        {
        scanf("%d",&l[i]);
        switch (l[i])
        {
        case 5: y[i]=1;
        break;
        case 6: y[i]=2;
        break;
        case 7: y[i]=3;
        break;
        case 8: y[i]=4;
        break;
        default:
        break;
        }
        z=y[i]+z;
        
        q=40+q;
        }
        d=z*20;
        
        sw=d+q;
        printf("Over time salary of month March: %d",sw);
    }

}

