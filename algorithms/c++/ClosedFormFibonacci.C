#include <cmath>
#include <iostream>
#include <string>

using namespace std;

unsigned long F(unsigned long n)
{
  return round(exp(n*log(1.6180339897) - 0.80471895621705));
}

int main(int argc, const char* argv[])
{
  std::cout << F(std::stol(argv[1])) << std::endl;
  return 0;
}
