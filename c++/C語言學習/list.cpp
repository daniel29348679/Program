#include <bits/stdc++.h>
using namespace std;
using namespace std::ranges;


template<typename type>
class listt {
public:
    class node {
public:
        node* root  = nullptr;
        node* child = nullptr;
        type thi;
    };
    class iterator {
public:
        node* p = nullptr;


        type& operator*()
        {
            return p->thi;
        }

        bool operator!=(const iterator&i)
        {
            return p != i.p;
        }

        iterator& operator++()
        {
            p = p->child;
            return *this;
        }
    };

private:
    int siz    = 0;
    node* head = nullptr;
    node* last = nullptr;

public:
    listt()
    {
        head = new node;
        last = head;
    }

    void push_back(type&t)
    {
        last->thi         = t;
        last->child       = new node;
        last->child->root = last;
        last = last->child;
        siz += 1;
    }

    iterator begin()
    {
        iterator i;

        i.p = head;
        return i;
    }

    iterator end()
    {
        iterator i;

        i.p = last;
        return i;
    }

    int size()
    {
        return siz;
    }

    bool empty()
    {
        return siz == 0;
    }
};


int main()
{
    vector<int> vec{100, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    listt<int>  li;

    for(auto i:vec)
        li.push_back(i);
    cout << li.size() << endl;

    for(auto i :li)
        cout << i;

    cout << "success!";


    //for(auto i:vec)
}
