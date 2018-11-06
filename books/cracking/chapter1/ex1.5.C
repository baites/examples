#include <cstdio>
#include <cstring>

using namespace std;

char * replace_spaces(const char * s) {
  size_t size = strlen(s);
  size_t counter = 0;
  for(size_t i=0; i<size; ++i)
    if(s[i] == ' ') ++counter;
  char * ns = new char[size + 2*counter];
  size_t j = 0;
  for(size_t i=0; i<size; ++i){
    if(s[i] == ' '){
      ns[j] = '%';
      ns[j+1] = '2';
      ns[j+2] = '0';
      j += 3;
    } else {
      ns[j] = s[i];
      j++;
    }
  }
  return ns;
}

int main() {
  char s[100] = "hola with spaces";
  printf("%s\n", s);
  char * ns = replace_spaces(s);
  printf("%s\n", ns);
  return 0;
}
