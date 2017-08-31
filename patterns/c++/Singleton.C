
#include <iostream>

#include "Singleton.h"

Singleton* Singleton::pInstance_ = 0;

int main()
{
    std::cout << Singleton::Instance()->ReturnInt() << std::endl;
    return 0;
}
