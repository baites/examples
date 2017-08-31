#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <utility>

long SimpleHash(std::string str, long size)
{
  long value = 0;
  for(unsigned i=0; i<str.length(); ++i) {
    value += std::pow(str[i], i);
  }
  return value % size;
}

typedef long (*HashFunc)(std::string, long);

template<typename T, HashFunc H>
class HashMap {

  typedef std::pair<std::string, T> PairType;
  typedef std::vector<PairType> ContainerType;

  ContainerType _container;
  long _size;

public:

  HashMap(long size = 13){
    _size = size;
    _container = ContainerType(size, std::make_pair("__nokey__", 0));
  };

  T& operator [] (const std::string & key)
  {
    long hashkey = H(key, _size);
    PairType *pair = &_container[hashkey];
    long counter = 1;
    while (pair->first != key && pair->first != "__nokey__")
    {
      hashkey = (hashkey + counter * (1+counter)) % _size;
      pair = &_container[hashkey];
      counter++;
    }
    pair->first = key;
    return pair->second;
  }

  friend std::ostream& operator<<(std::ostream& os, const HashMap<T,H>& obj)
  {
    for(typename HashMap<T,H>::ContainerType::const_iterator itr = obj._container.begin(); itr != obj._container.end(); ++itr) {
      os << "Key: " << itr->first << " Value: " << itr->second << std::endl;
    }
    return os;
  }
};
