#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
string s;
cout<<"Enter a sentence: ";
getline(cin,s);
reverse(s.begin(),s.end());
cout<<"\n"<<s;
cout<<"\n";
}
