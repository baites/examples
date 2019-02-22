
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
        stype l = 0;
        stype r = 0;

        // Binary search
        while(1) {
            if(m >= r1-1)
                l = max(m-r1+1,l2);
            else
                l = l2;
            r = min(m-l1+1,r2);
            m2 = (l+r)/2;
            m1 = m-m2;
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
        if(m1 < S1 && m2 < S2){
            return min(A1[m1],A2[m2]);
        } else if (m2 == S2) {
            return A1[m1];
        } else {
            return A2[m2];
        }
    }

    double findMedianSortedArrays(vtype& A1, vtype& A2) {
        stype S1 = A1.size();
        stype S2 = A2.size();
        stype S = S1 + S2;
        double median1 = 0;
        bool isEdge = isEdgeCase(median1, A1, S1, A2, S2);
        if(isEdge)
            return median1;
        median1 = findMedianHelper(A1, S1, A2, S2);
        if(S % 2)
            return median1;
        if(A1.back() > A2.back())
            S1 -= 1;
        else
            S2 -= 1;
        double median2 = findMedianHelper(A1, S1, A2, S2);
        return 0.5*(median1 + median2);
    }
};

int main()
{
    stype size = 40000000;
    stype maxv = 1000000;

    default_random_engine engine;
    uniform_int_distribution<int> dist2(-maxv, maxv);

    auto generator = [&dist2, &engine]() {
        return dist2(engine);
    };

    vector<int> A1(size);
    generate(begin(A1), end(A1), generator);
    sort(begin(A1), end(A1));

    vector<int> A2(size);
    generate(begin(A2), end(A2), generator);
    sort(begin(A2), end(A2));

    typedef chrono::high_resolution_clock myclock;
    myclock::time_point start = myclock::now();
    cout << Solution().findMedianSortedArrays(A1, A2) << endl;
    myclock::duration delta = myclock::now() - start;
    cout << "time: " << chrono::duration_cast<chrono::microseconds>(delta).count() << endl;
    return 0;
}
