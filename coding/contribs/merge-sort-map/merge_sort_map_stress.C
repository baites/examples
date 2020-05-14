
#include <algorithm>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

typedef vector<int> vtype;
typedef vector<int>::size_type stype;


class Naive {
public:

    int mergeSortMap(vtype& A1, vtype& A2, stype I) {
        vtype A = A1;
        A.insert(A.end(), A2.begin(), A2.end());
        sort(A.begin(), A.end());
        stype S = A.size();
        return A[I];
    }
};


class Solution {
public:

    int mergeSortMap(vtype& A1, vtype& A2, stype I){

        // Array size
        stype S1 = A1.size();
        stype S2 = A2.size();
        stype S = S1 + S2;
        stype m = S/2;

        // Sanity check
        if (S == 0)
            throw runtime_error("empty both arrays");
        if (I < 0 || I >= S)
            throw std::out_of_range ("merge-sort map index out of range");

        // Edge cases
        if (S1 == 0)
            return A2[I];
        if (S2 == 0)
            return A1[I];

        // Interval initialization
        stype l1 = 0;
        stype r1 = S1+1;
        stype l2 = 0;
        stype r2 = S2+1;
        stype i1 = 0;
        stype i2 = 0;
        stype l = 0;
        stype r = 0;

        // Binary search
        while(1) {
            if(I >= r1-1)
                l = max(I-r1+1,l2);
            else
                l = l2;
            r = min(I-l1+1,r2);
            i2 = (l+r)/2;
            i1 = I-i2;
            if(i1 > 0 && i2 < S2 && A1[i1-1] > A2[i2]){
                r1 = i1;
                l2 = i2+1;
            } else if (i2 > 0 && i1 < S1 && A2[i2-1] > A1[i1]){
                l1 = i1+1;
                r2 = i2;
            } else {
                break;
            }
        }
        int value;
        if(i1 < S1 && i2 < S2){
            value = min(A1[i1],A2[i2]);
        } else if (i2 == S2) {
            value = A1[i1];
        } else {
            value = A2[i2];
        }
        return value;
    }
};


int main()
{
    stype tries = 20;
    stype maxs = 4000000;
    stype maxv = 10000000;

    typedef chrono::high_resolution_clock myclock;
    myclock::time_point start = myclock::now();

    myclock::duration delta = myclock::now() - start;
    unsigned seed = delta.count();

    default_random_engine engine;
    engine.seed(seed);

    uniform_int_distribution<int> dist1(0, maxs);
    uniform_int_distribution<int> dist2(-maxv, maxv);

    auto generator = [&dist2, &engine]() {
        return dist2(engine);
    };

    for(stype i = 0; i<tries; ++i) {

        dist1(engine);
        stype S1 = dist1(engine);
        stype S2 = dist1(engine);

        if(S1 == 0 && S2 == 0)
            continue;

        vector<int> A1(S1);
        generate(begin(A1), end(A1), generator);
        sort(begin(A1), end(A1));

        vector<int> A2(S2);
        generate(begin(A2), end(A2), generator);
        sort(begin(A2), end(A2));

        uniform_int_distribution<int> dist3(0, S1+S2-1);
        stype I = dist3(engine);

        auto refs = Naive().mergeSortMap(A1, A2, I);
        auto test = Solution().mergeSortMap(A1, A2, I);

        if(test != refs) {
            cout << "Error" << endl;
            /*for (auto v : A1)
                cout << v << " ";
            cout << endl;

            for (auto v : A2)
                cout << v << " ";
            cout << endl;*/

            cout << refs << endl;
            cout << test << endl;
            break;
        }
        cout << refs << endl;
        cout << test << endl;
    }

    return 0;
}
