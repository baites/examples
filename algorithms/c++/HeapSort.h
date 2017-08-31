#include <cmath>
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
void exchange(
  T & container,
  typename T::size_type i,
  typename T::size_type j
){
  typename T::value_type tmp = container[i];
  container[i] = container[j];
  container[j] = tmp;
}


template <typename T>
void maxHeap(
  T & container,
  typename T::size_type i,
  typename T::size_type heapsize
){
  typename T::size_type l = 2*i+1;
  typename T::size_type r = 2*i+2;
  typename T::size_type largest = i;
  if(l < heapsize && container[l] > container[i])
    largest = l;
  if(r < heapsize && container[r] > container[largest])
    largest = r;
  if(largest != i) {
    exchange(container, i, largest);
    maxHeap(container, largest, heapsize);
  }
}


template <typename T>
void buildMaxHeap(T & container)
{
  typename T::size_type heapsize = container.size();
  typename T::size_type index = heapsize/2;
  do {
    --index;
    maxHeap(container, index, heapsize);
  } while(index != 0);
}


template <typename T>
void heapsort(T & container)
{
  typename T::size_type heapsize = container.size();
  buildMaxHeap(container);
  do {
    --heapsize;
    exchange(container, 0, heapsize);
    maxHeap(container, 0, heapsize);
  } while(heapsize != 1);
}
