#include <iostream>
#include <string>

using namespace std;

class LifetimeProbe {
    string payload;
public:
    LifetimeProbe()
    {
        cout << "...probe constructor " << &(*this) << endl;
        payload = "payload value";
    }
    LifetimeProbe(const LifetimeProbe & o)
    {
        cout << "...probe copy constructor " << &(*this) << " from " << &o << endl;
    }
    ~LifetimeProbe()
    {
        cout << "...probe destruction " << &(*this) << endl;
    }
    const string & getPayload() const
    {
        return payload;
    }
};

const LifetimeProbe & CreateLocalProve()
{
    LifetimeProbe probe;
    return probe;
}

int main(int argc, const char* argv[])
{
    cout << "creating local probe" << endl;
    const LifetimeProbe & probe = CreateLocalProve();
    cout << "created local probe" << endl;
    cout << "calling probe.getPayload()" << endl;
    cout << "payload value: " << probe.getPayload() << endl;
    cout << "called probe.getPayload()" << endl;
    return 0;
}
