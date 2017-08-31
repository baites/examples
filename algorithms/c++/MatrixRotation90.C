#include <cmath>
#include <iostream>

using namespace std;

#define n 3

int M[n][n] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};

void print_matrix(int (&M)[n][n])
{
  for(int i=0; i<n; ++i) {
    for(int j=0; j<n; ++j)
      cout << M[i][j] << " ";
    cout << endl;
  }
  cout << endl;
}

void rotate_matrix(int (&M)[n][n])
{
  int m = ceil(n/2);
  for(int i=0; i<m; ++i)
  {
    for(int j=i; j<(n-1-i); ++j)
    {
      int t1 = M[n-1-i][j];
      M[n-1-i][j] = M[j][i];
      int t2 = M[n-1-j][n-1-i];
      M[n-1-j][n-1-i] = t1;
      t1 = M[i][n-1-j];
      M[i][n-1-j] = t2;
      M[j][i] = t1;
    }
  }
}

int main() {
  print_matrix(M);
  rotate_matrix(M);
  print_matrix(M);
  return 0;
}
