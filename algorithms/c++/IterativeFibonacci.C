#include <iostream>
#include <string>

// Fibonacci iterative algorithm.
double F(unsigned int n)
{
  if (n < 2)
    return n;
  double F2 = 0;
  double F1 = 1;
  double F0;
  for(unsigned int i=2; i<=n; ++i)
  {
      F0 = F1 + F2;
      F2 = F1;
      F1 = F0;
  }
  return F0;
}

int main(int argc, const char* argv[])
{
  std::cout.precision(17);
  std::cout << F(std::stol(argv[1])) << std::endl;
  return 0;
}
