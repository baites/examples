#! /usr/bin/env node

function Exchange(A, i, j) {
  const t = A[i];
  A[i] = A[j];
  A[j] = t;
}

function Partition(A, p, r) {
  const x = A[r-1];
  let i = p - 1;
  for (let j=p; j<(r-1); j++) {
    if (A[j] <= x) {
      i += 1;
      Exchange(A, i, j);
    }
  }
  Exchange(A, i+1, r-1);
  return i+1;
}

function QuickSort(A, p, r) {
  if (p < r - 1){
    const q = Partition(A, p, r);
    QuickSort(A, p, q-1);
    QuickSort(A, q+1, r);
  }
}

const A = [2, 8, 7, 1, 3, 5, 6, 4];
QuickSort(A, 0, A.length);

console.log(A);
