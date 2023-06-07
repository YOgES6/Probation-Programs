#include<iostream>
#include<cstring>
using namespace std;

int main()
{
char symbol[10]={'.' ,':' ,',' ,'!'};
char l[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
string s;
int y,i,k,f,j,m=0,n=0,o=0;

cout<<"Enter a sentence";
getline(cin,s);
y=s.length();
cout<<"\n"<<y<<"\n\n";

for(i=0; i<=y; i++)
{
for(int d=0; d<=25; d++)
{
if(s[i]==l[d])
{
m++;
}
}  
}


for(j=0; j<=y; j++)
{
for(int h=0; h<=4; h++)
{
if(s[j]==symbol[h])
{
n++;
}
} 
}
o=s.find(" ",o);


cout<<"\n"<<"Upper case: "<<m<<"\n"<<"Symbols: "<<n<<"\n"<<"White space: "<<o;

}
