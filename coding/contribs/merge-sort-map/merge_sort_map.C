
#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

typedef vector<int> vtype;
typedef vector<int>::size_type stype;

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
    vector<int> A1 {-2, -2, -1, 0, 2, 5};
    vector<int> A2 {-9, -2, 1, 10};

    cout << Solution().mergeSortMap(A1, A2, 5) << endl;
    return 0;
}
