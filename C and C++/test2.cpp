#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;


int main()
{
ofstream myfile("found.dat");
string s;
cout<<"1.Enter a sentence: ";
getline(cin,s);
myfile<<s;
myfile.close();
cout<<"Done well...";

ofstream myfile1("found1.dat");
string s1;
cout<<"\n2.Enter a sentence: ";
getline(cin,s1);
myfile1<<s1;
myfile1.close();
cout<<"Done well...";

ifstream file("found.dat");
string y;
while(getline(file,y))

cout<<y;

cout<<"Done well...";


ifstream file1("found1.dat");
string y1;
while(getline(file1,y1))

cout<<y1;

cout<<"Done well...";

int i=0;
while(y[i]!='\0' || y1[i]!='\0')
{
if(y[i]!=y1[i])
{
ofstream myfile6("file.dat");
myfile6<<y1[i];
myfile6.close();
}

else
{
ofstream myfile6("file.dat");
myfile6<<"Files are same";
}
i++;
}

system("file.dat");
}
