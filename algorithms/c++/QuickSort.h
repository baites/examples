#include <iostream>


template <typename T>
void printA(const T & container)
{
  for(typename T::const_iterator iter = container.begin(); iter != container.end(); ++iter)
  {
    std::cout << *iter << " ";
  }
  std::cout << std::endl;
}


template <typename T>
void exchange(T & container, typename T::size_type i, typename T::size_type j)
{
  typename T::value_type tmp = container[i];
  container[i] = container[j];
  container[j] = tmp;
}


template <typename T>
typename T::size_type partition(T & container, typename T::size_type p, typename T::size_type r)
{
  bool init = true;
  typename T::size_type i = p;
  for(typename T::size_type j = p; j < r; ++j)
  {
    if(container[j] < container[r])
    {
      if(!init) ++i;
      else init = false;
      exchange(container, i, j);
    }
  }
  if(init == true)
    exchange(container, i, r);
  else
    exchange(container, i+1, r);
  return i+1;
}


template <typename T>
void quicksort(T & container, typename T::size_type k, typename T::size_type r)
{
  if (k < r)
  {
    typename T::size_type p = partition(container, k, r);
    quicksort(container, k, p-1);
    quicksort(container, p+1, r);
  }
}
