#include <cstdio>
#include <cstring>

using namespace std;

void reverse_c_string(char * s){
  char * l = s;
  char * r = s;
  for(int i=0; i<strlen(s) - 1; ++i)
    r++;
  while(l < r) {
    char temp = '\0';
    temp = *l;
    *l = *r;
    *r = temp;
    l++;
    r--;
  }
}


int main (int argc, const char * argv[]){
  char s[] = "hola";
  reverse_c_string(s);
  printf("%s\n", s);
  return 0;
}
