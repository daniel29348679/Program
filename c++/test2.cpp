#include <bits/stdc++.h>
using namespace std;


class node_avl
{
public:
    int h = 0;
    list<int> li;
    shared_ptr<node_avl> root = nullptr;
    vector<shared_ptr<node_avl> > child {nullptr, nullptr};

    void checkandchangeh()
    {
        h = 1 + max((child[0] == nullptr)? -1:child[0]->h, (child[1] == nullptr)? -1:child[1]->h);
    }

    int heightl_r()
    {
        return ((child[0] == nullptr)? -1:child[0]->h) - ((child[1] == nullptr)? -1:child[1]->h);
    }
};

shared_ptr<node_avl> head = nullptr;
void rotater(shared_ptr<node_avl> node)
{
    if(node == nullptr || (node->child[0] == nullptr && node->child[1] == nullptr))
        return;

    cout << "right rotate,";
    shared_ptr<node_avl> nnode = make_shared<node_avl>();
    swap(node->li, nnode->li);
    if(node->child[0] != nullptr)
    {
        swap(node->li, node->child[0]->li);
        nnode->child[0] = node->child[0]->child[1];
        if(nnode->child[0] != nullptr)
            nnode->child[0]->root = nnode;
    }
    nnode->child[1] = node->child[1];
    if(nnode->child[1] != nullptr)
        nnode->child[1]->root = nnode;
    if(node->child[0] != nullptr)
    {
        node->child[0] = node->child[0]->child[0];
        if(node->child[0] != nullptr)
            node->child[0]->root = node;
    }
    node->child[1] = nnode;
    nnode->root    = node;
    nnode->checkandchangeh();
}

void rotatel(shared_ptr<node_avl> node)
{
    if(node == nullptr || (node->child[0] == nullptr && node->child[1] == nullptr))
        return;

    cout << "left rotate,";
    shared_ptr<node_avl> nnode = make_shared<node_avl>();
    swap(node->li, nnode->li);
    if(node->child[1] != nullptr)
    {
        swap(node->li, node->child[1]->li);
        nnode->child[1] = node->child[1]->child[0];
        if(nnode->child[1] != nullptr)
            nnode->child[1]->root = nnode;
    }
    nnode->child[0] = node->child[0];
    if(nnode->child[0] != nullptr)
        nnode->child[0]->root = nnode;
    if(node->child[1] != nullptr)
    {
        node->child[1] = node->child[1]->child[1];
        if(node->child[1] != nullptr)
            node->child[1]->root = node;
    }
    node->child[0] = nnode;
    nnode->root    = node;
    nnode->checkandchangeh();
}

void checkandrotate(shared_ptr<node_avl> node)
{
    if(node == nullptr)
        return;

    int h = node->h;

    cout << "height-" << node->heightl_r() << ",";
    if(node->heightl_r() > 1)     //right rotate
    {
        if(node->child[0]->heightl_r() < 0)
            rotatel(node->child[0]);
        rotater(node);
    }

    if(node->heightl_r() < -1)     //left rotate
    {
        if(node->child[1]->heightl_r() > 0)
            rotater(node->child[1]);
        rotatel(node);
    }

    node->checkandchangeh();
    if(node->h != h)
        checkandrotate(node->root);
}

void push(int i, shared_ptr<node_avl>& node)
{
    if(node == nullptr)
    {
        node = make_shared<node_avl>();
        node->li.push_back(i);
        return;
    }
    if(i < *node->li.begin())
    {
        cout << "l,";
        if(node->child[0] != nullptr)
        {
            push(i, node->child[0]);
            return;
        }
        node->child[0]       = make_shared<node_avl>();
        node->child[0]->root = node;
        node->child[0]->li.push_back(i);
        node->child[0]->checkandchangeh();
        checkandrotate(node);
        return;
    }
    if(i == *node->li.begin())
    {
        node->li.push_back(i);
        return;
    }
    if(i > *node->li.begin())
    {
        cout << "r,";
        if(node->child[1] != nullptr)
        {
            push(i, node->child[1]);
            return;
        }
        node->child[1]       = make_shared<node_avl>();
        node->child[1]->root = node;
        node->child[1]->li.push_back(i);
        node->child[1]->checkandchangeh();
        checkandrotate(node);
        return;
    }
}

int main()
{
    int i;

    while(cin >> i)
    {
        cout << "pushing " << i << " :";
        push(i, head);
        cout << endl;
        cout << "root" << *head->li.begin();
        cout << endl;
    }
}
