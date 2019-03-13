
#include <algorithm>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

typedef vector<int> vtype;
typedef vector<int>::size_type stype;

class Solution {
public:
    ///cantidad de numeros menores o iguales a val
    double findMedianSortedArray(vtype& A, stype S)
    {
        auto m = S/2;
        if(S % 2)
            return A[m];
        return 0.5*(A[m]+A[m-1]);
    }

    bool isEdgeCase(double& median, vtype& A1, stype S1, vtype& A2, stype S2)
    {
        auto S = S1 + S2;
        auto m = S/2;

        // One empty array
        if(S1 == 0) {
            median = findMedianSortedArray(A2, S2);
            return true;
        }
        if(S2 == 0) {
            median = findMedianSortedArray(A1, S1);
            return true;
        }

        // None overlaping arrays
        if(A1.back() < A2.front()) {
            if (S % 2) {
                if(S1 > m) {
                    median = A1[m];
                    return true;
                } else {
                    median = A2[m-S1];
                    return true;
                }
            } else {
                if(S1 > m) {
                    median = 0.5*(A1[m]+A1[m-1]);
                    return true;
                } else if (m > S1) {
                    median = 0.5*(A2[m-S1]+A2[m-1-S1]);
                    return true;
                } else {
                    median = 0.5*(A2.front()+A1.back());
                    return true;
                }
            }
        } else if(A2.back() < A1.front())
        {
            if (S % 2) {
                if(S2 > m) {
                    median = A2[m];
                    return true;
                } else {
                    median = A1[m-S2];
                    return true;
                }
            } else {
                if(S2 > m) {
                    median = 0.5*(A2[m]+A2[m-1]);
                    return true;
                } else if (m > S2) {
                    median = 0.5*(A1[m-S2]+A1[m-1-S2]);
                    return true;
                } else {
                    median = 0.5*(A1.front()+A2.back());
                    return true;
                }
            }
        }
        return false;
    }

    double findMedianHelper(vtype& A1, stype S1, vtype& A2, stype S2){
        // Array size
        stype S = S1 + S2;
        stype m = S/2;
        stype l1 = 0;
        stype r1 = S1+1;
        stype l2 = 0;
        stype r2 = S2+1;
        stype m1 = 0;
        stype m2 = 0;
        stype count = 0;

        cout << "count l1 i1 r1 l2 i2 r2" << endl;

        // Binary search
        while(1) {
            if(m >= r1-1)
                l2 = max(m-r1+1,l2);
            r2 = min(m-l1+1,r2);
            m2 = (l2+r2)/2;
            m1 = m-m2;
            cout << ++count << " " << l1 << " " << m1 << " " << r1;
            cout << " " << l2 << " " << m2 << " " << r2 << endl;
            if(m1 > 0 && m2 < S2 && A1[m1-1] > A2[m2]){
                r1 = m1;
                l2 = m2+1;
            } else if (m2 > 0 && m1 < S1 && A2[m2-1] > A1[m1]){
                l1 = m1+1;
                r2 = m2;
            } else {
                break;
            }
        }
        double median1;
        if(m1 < S1 && m2 < S2){
            median1 = min(A1[m1],A2[m2]);
        } else if (m2 == S2) {
            median1 = A1[m1];
        } else {
            median1 = A2[m2];
        }
        if(S%2)
            return median1;
        stype n1;
        stype n2;
        if(m1 == 0) {
            n1 = m1;
            n2 = m2-1;
        } else if(m2 == 0) {
            n1 = m1-1;
            n2 = m2;
        } else {
            n1 = m1-1;
            n2 = m2;
            if(
                n1 > 0 && n2 < S2 && A1[n1-1] > A2[n2] ||
                n2 > 0 && n1 < S1 && A2[n2-1] > A1[n1]
            ) {
                n1 = m1;
                n2 = m2-1;
            }
        }
        double median2;
        if(n1 < S1 && n2 < S2){
            median2 = min(A1[n1],A2[n2]);
        } else if (n2 == S2) {
            median2 = A1[n1];
        } else {
            median2 = A2[n2];
        }
        return 0.5*(median1+median2);
    }

    double findMedianSortedArrays(vtype& A1, vtype& A2) {
        stype S1 = A1.size();
        stype S2 = A2.size();
        stype S = S1 + S2;
        return findMedianHelper(A1, S1, A2, S2);
    }
};

int main()
{
    stype size = 8;

    //vector<int> A1 {0};
    //A1.insert(end(A1), size, 1);

    //vector<int> A2(size-1, -1);
    //A2.insert(end(A2), 1, 0);
    vector<int> A1(size, 1);
    vector<int> A2(size-1, -1);


    typedef chrono::high_resolution_clock myclock;
    myclock::time_point start = myclock::now();
    cout << Solution().findMedianSortedArrays(A1, A2) << endl;
    myclock::duration delta = myclock::now() - start;
    cout << "time: " << chrono::duration_cast<chrono::microseconds>(delta).count() << endl;
    return 0;
}
