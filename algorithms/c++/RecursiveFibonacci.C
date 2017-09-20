#include <iostream>
#include <string>

unsigned long F(unsigned long n)
{
  if (n < 2)
    return n;
  return F(n-1) + F(n-2);
}

int main(int argc, const char* argv[])
{
  std::cout << F(std::stol(argv[1])) << std::endl;
  return 0;
}
