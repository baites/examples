#! /usr/bin/env node

function Merge(A, p, q, r) {
  const L = A.slice(p, q);
  const R = A.slice(q, r);
  let i = 0;
  let j = 0;
  for (let k=p; k<r; k++) {
    if (i === L.length && j === R.length) {
      return;
    }
    if (i === L.length) {
      A[k] = R[j];
      j++;
    } else if (j === R.length) {
      A[k] = L[i];
      i++;
    } else if (L[i] <= R[j]) {
      A[k] = L[i];
      i++;
    } else {
      A[k] = R[j];
      j++;
    }
  }
}

function MergeSort(A, p, r) {
  if(p < r - 1) {
    const q = Math.floor((p+r)/2);
    MergeSort(A, p, q);
    MergeSort(A, q, r);
    Merge(A, p, q, r);
  }
}

A = [2, 8, 7, 1, 3, 5, 6, 4];
MergeSort(A, 0, A.length);


console.log(A);
