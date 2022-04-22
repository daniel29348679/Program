#include<bits/stdc++.h>
using namespace std;
int total=0,x=0,y=0;
int mapp[1000][1000];
int bx=-1,by=-1,bxx=-1,byy=-1;


void run(int i,int j,int xx,char way)
{
    if(!(0<=i&&i<x&&0<=j&&j<y)) return;
    if(mapp[i][j]==-10)return;
    if(mapp[i][j]>xx+1)
    {
        mapp[i][j]=xx+1;
        if(way!='R') run(i,j+1,xx+1,'L');
        if(way!='L') run(i,j-1,xx+1,'R');
        if(way!='U') run(i-1,j,xx+1,'D');
        if(way!='D') run(i+1,j,xx+1,'U');

    }
}


string findd(int i,int j,int xx,string way)
{
    string str;
    if(!(0<=i&&i<x&&0<=j&&j<y)) return "";
    if(mapp[i][j]==-10)return "";
    if(mapp[i][j]!=xx+1)return "";

    if(i==bxx&j==byy) return way+"Y";

    str+=findd(i,j+1,xx+1,"R");
    if(str[str.length()-1]=='Y')return way+str;
    str+=findd(i,j-1,xx+1,"L");
    if(str[str.length()-1]=='Y')return way+str;
    str+=findd(i-1,j,xx+1,"U");
    if(str[str.length()-1]=='Y')return way+str;
    str+=findd(i+1,j,xx+1,"D");
    if(str[str.length()-1]=='Y')return way+str;
    return "";


}

int main()
{
    ifstream cinn("test_input.txt");
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cinn>>x>>y;

    //memset(mapp,-1,sizeof(mapp));
    char ch;
    for(int i=0;i<x;i++)
        for(int j=0;j<y;j++)
        {
            cinn>>ch;
            if(ch=='.')
            {
                mapp[i][j]=100000;
            }
            else if(ch=='A')
            {
                bx=i;
                by=j;
                //cout<<i<<j<<bx<<by<<"\n";
                mapp[i][j]=100001;
            }
            else if(ch=='B')
            {
                bxx=i;
                byy=j;
                mapp[i][j]=100002;
            }
            else mapp[i][j]=-10;
        }


    if(bx==-1||bxx==-1){
        cout<<"NO";
        return 0;
    }



    //cout<<bx<<" "<<by<<"\n";
    run(bx,by,0,'\0');

    //for(int i=0;i<x;i++){for(int j=0;j<y;j++){printf("%6d ",mapp[i][j]);}printf("\n");}

    if(mapp[bxx][byy]==100002){
        cout<<"NO";
        return 0;
    }
    return 0;
    string st=findd(bx,by,0,"");
    st.erase(st.length()-1);
    cout<<"YES\n"<<st.length()<<"\n"<<st;

}