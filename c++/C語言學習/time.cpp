#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int a=100;
    int ti=clock();
    for(int i=0;i<(int)1e4;i++)printf("%d",a);
    int ti2=clock();
	for(int i=0;i<(int)1e4;i++)cout<<a;
    cout<<"\n\ncout COST   "<<(float)(clock()-ti2)/1000<<"s";
	cout<<"\n\nprintf COST "<<(float)(ti2-ti)/1000<<"s";
}