#include "HashMap.h"

#include <iostream>

int main() {
  HashMap<int, SimpleHash> hmap;
  hmap["dog"] = 1;
  hmap["cat"] = 2;
  hmap["lion"] = 3;
  hmap["music"] = 4;
  std::cout << hmap << std::endl;
  return 0;
}
