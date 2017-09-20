#include <iostream>
#include <string>

unsigned long F(unsigned long n)
{
  if (n < 2)
    return n;
  unsigned long F2 = 0;
  unsigned long F1 = 1;
  unsigned long F0;
  for(unsigned long i=2; i<=n; ++i)
  {
      F0 = F1 + F2;
      F2 = F1;
      F1 = F0;
  }
  return F0;
}

int main(int argc, const char* argv[])
{
  std::cout << F(std::stol(argv[1])) << std::endl;
  return 0;
}
