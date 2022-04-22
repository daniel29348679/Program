#include<bits/stdc++.h>
using namespace std;

struct test
{
    int x;
    test* next=NULL;
    test* front=NULL;
};
test* arr(test* head,int i)
{
    for(;i>0;i--) head=(*head).next;
    return head;
}

void loc(test* &lo,int i)
{
    for(;i>0;i--)
    {
        if(lo->next==NULL)
        {
            cout<<"Broken!!!!"<<endl;
            return ;
        }
        lo=lo->next;
    }
    for(;i<0;i++)
    {
        if(lo->front==NULL)
        {
            cout<<"Broken!!!!"<<endl;
            return ;
        }
        lo=lo->front;
    }
};


int main()
{
    test* head=new test;
    test* temp;
    test* end;
    temp=head;
    for(int i=0;i<100;i++,temp=(*temp).next)
    {
        (*temp).x=2*i;
        (*temp).next=new test;
        temp->next->front=temp;
        end=temp;
    }
    temp->front->next=NULL;

    for(temp=head;temp!=NULL;temp=(*temp).next)
    {
        cout<<(*temp).front<<" "<<(*temp).x<<" "<<(*temp).next<<endl;
    }
    for(temp=end;temp!=NULL;temp=(*temp).front)
    {
        cout<<(*temp).front<<" "<<(*temp).x<<" "<<(*temp).next<<endl;
    }

    while(1)
    {
        int k;
        cin>>k;
        cout<<(*arr(head,k)).x<<endl;
    }



}