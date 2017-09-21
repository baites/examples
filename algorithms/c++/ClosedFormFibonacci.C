#include <cmath>
#include <iostream>
#include <string>

using namespace std;

double F(unsigned int n)
{
  return round(exp(n*log(1.6180339897L) - 0.80471895621705L));
}

int main(int argc, const char* argv[])
{
  std::cout.precision(17);
  std::cout << F(std::stol(argv[1])) << std::endl;
  return 0;
}
