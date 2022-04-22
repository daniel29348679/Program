#include<bits/stdc++.h>
using namespace std;

struct FullOrNot{
    char ch = '\0' ;
    bool full = 0 ;
    FullOrNot * next ;
};

int main() {
    // 辨識字母、計算字母數，只有一種字母是奇數個 
    // 依出現順序正著印 印奇數 再倒著印
    string str ;
    cin >> str ;
    FullOrNot * head = NULL ;
    FullOrNot * p = NULL ;
    bool found ;
    for ( long int i = 0 ; str[i] != '\0' ; i++ ) {
        found = 0 ;
        p = head ;
        if ( head == NULL ) { 
            head = new FullOrNot ;
            head -> ch = str[i] ;
            found = 1 ;
        }
            
        while( p != NULL && !found ) {
            if ( str[i] == p -> ch && !(p -> full) ) p -> full = 1 ;
            p = p -> next ;
        }
        
        if ( !found ) {
            p = new FullOrNot ;
            p -> ch = str[i] ;
        }
    } // 有i個字母 
    
    p = head ;
    long int count = 0 ;
    while( p != NULL ) {
        if( !(p->full) ) count++ ;
        p = p -> next ;
    }
    if ( count >= 2 ) {
        cout << "NO SOLUTION" ; 
        return 0 ;
    }
    
    // 印東西 
    int n = i/2 ;
    char printorder[n] = {'\0'} ;
    i = 0 ;
    char theodd = '\0' ;
    p = head ;
    while ( p != NULL ) {
        if ( p -> full ) {
            printorder[i] = p -> ch ;
            i++ ;
        } 
        else  theodd = p -> ch ;    
        p = p -> next ;
    }
    for ( long int j = 0 ; j < i ; j++ ) 
        cout << printorder[j] ;
    if ( theodd != '\0' )  cout << theodd ;
    for ( ; i>0 ; i--) 
        cout << printorder[i] ;
}