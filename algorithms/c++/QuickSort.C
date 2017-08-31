#include <vector>

#include "QuickSort.h"

using namespace std;


int main(int argc, const char* argv[])
{
  vector<int> array = {2, 8, 7, 1, 3, 5, 6, 4};
  printA(array);
  quicksort(array, 0, array.size()-1);
  printA(array);
}
