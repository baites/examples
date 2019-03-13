#include <iostream> // includes cin to read from stdin and cout to write to stdout
#include <map>
#include <set>
#include <list>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cassert>
#include <math.h>
#include <iomanip>
#include <limits>

#include <chrono>
#include <random>


///LLONG_MAX,INT_MA
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define amfor(Iterator, Container)     for ( auto Iterator = begin(Container); (Iterator) != end(Container); ++(Iterator) )
#define ramfor(Iterator, Container) for ( auto Iterator = Container.rbegin(); (Iterator) != Container.rend(); ++(Iterator) )
template<class C, class E> inline bool contains(const C& container, const E& element) { return container.find(element) != container.end(); }
#define  NP(nn,ta,a,tb,b) struct nn : pair<ta,tb> { nn():pair<ta,tb>(){}; nn(ta pa,tb pb):pair<ta,tb>(pa,pb){} ta& a(){return first;} tb& b(){return second;} };
template<class T> inline void checkmin(T &a, T b) { if (b < a) a = b; }//asigna en a el minimo
template<class T> inline void checkmax(T &a, T b) { if (b > a) a = b; }//asigna en a el maximo


typedef long long ll;
using namespace std; // since cin and cout are both in namespace std, this saves some text
typedef vector<ll> vll;
typedef vector<vector<ll>> vvll;

typedef vector<int> vtype;
typedef vector<int>::size_type stype;

class Solution {
public:
    ///cantidad de numeros menores o iguales a val
    int Search(int val, vector<int>& nums1, vector<int>& nums2, int &count1, int &count2)
    {
        count1 = std::upper_bound(all(nums1), val) - nums1.begin();
        count2 = std::upper_bound(all(nums2), val) - nums2.begin();
        return count1 + count2;
    }

    double Solve(int firstLarger,vector<int>& nums1, vector<int>& nums2, int count1, int count2)
    {
        int total = (nums1.size() + nums2.size());
        int searchedCount = (total + 1) / 2;
        int found = count1 + count2;
        if (found > searchedCount)
            return firstLarger;
        if (total % 2 == 1)
            return firstLarger;
        ///busco el siguiente
        int nextVal;
        if (count1 != nums1.size())
        {
            nextVal = nums1[count1];
            if (count2 != nums2.size())
                checkmin(nextVal, nums2[count2]);
        }
        else
            nextVal = nums2[count2];
        return (firstLarger + nextVal) / 2.0;
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        if (nums1.empty())
            return (nums2[nums2.size() / 2] + nums2[(nums2.size() - 1) / 2]) / 2.0;
        if (nums2.empty())
            return (nums1[nums1.size() / 2] + nums1[(nums1.size() - 1) / 2]) / 2.0;

        int total = (nums1.size() + nums2.size());
        int searchedCount = (total+1)/2;
        int count1, count2;
        ll minVal = min(nums1.front(), nums2.front());
        int minCount = Search(minVal ,nums1, nums2, count1, count2);
        if (minCount >= searchedCount)
            return Solve(minVal, nums1, nums2, count1, count2);
        ll minCant = minVal;
        ll maxCan = max(nums1.back(), nums2.back());
        while (minCant+1 != maxCan)
        {
            ll mid = (minCant + maxCan) / 2;
            int cc = Search(mid, nums1, nums2, count1, count2);
            if (cc >= searchedCount)
                maxCan = mid;
            else
                minCant = mid;
        }
        Search(maxCan, nums1, nums2, count1, count2);
        return Solve(maxCan, nums1, nums2, count1, count2);
    }
};

int main()
{
    stype size = 500000000;

    vector<int> A1 {0};
    A1.insert(end(A1), size, 1);

    vector<int> A2(1, -1);
    A2.insert(end(A2), 1, 0);

    typedef chrono::high_resolution_clock myclock;
    myclock::time_point start = myclock::now();
    cout << Solution().findMedianSortedArrays(A1, A2) << endl;
    myclock::duration delta = myclock::now() - start;
    cout << "time: " << chrono::duration_cast<chrono::microseconds>(delta).count() << endl;
    return 0;
}
