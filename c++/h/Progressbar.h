#include <bits/stdc++.h>

void printprogress(float i)
{

    std::cout << "\rcompleted:[" << std::string(i / 2, '|')
    << std::string(50 - int(i / 2), ' ')
    << "]" << i << "%" << std::flush;
}
