#include<iostream>
#include<fstream>
using namespace std;

int main()
{
string s,y;
int l1,l2;
cout<<"Enter a sentence: ";
getline(cin,s);
cout<<"Enter a sentence: ";
getline(cin,y);
l1=s.length();
l2=y.length();
for(int i=0,k=0; i<=l1,k<=l2; i++,k++)
{
if(s[i]!=y[k])
{
cout<<y[k];
}

ofstream myfile1("found.dat");
myfile1<<y[k];
}

cout<<"\n\n";
}
