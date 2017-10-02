#include <cstdlib>
#include <functional>
#include <iostream>
#include <string>
#include <tuple>

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

tuple<function<LifetimeProbe()>, function<void(LifetimeProbe)>> CreateMethods(LifetimeProbe context)
{
    return {
        [&]() { return context; },
        [&](LifetimeProbe value) { context = value; }
    };
}

int main(int argc, const char* argv[])
{
    cout << "creating context methods" << endl;
    auto [getContext, setContext] = CreateMethods(LifetimeProbe());
    cout << "created context" << endl;
    cout << "calling getContext().getPayload()" << endl;
    cout << "payload value: " << getContext().getPayload() << endl;
    cout << "called getContext().getPayload()" << endl;
    cout << "calling setContext(LifetimeProbe())" << endl;
    setContext(LifetimeProbe());
    cout << "called setContext(LifetimeProbe())" << endl;
    cout << "calling getContext().getPayload()" << endl;
    cout << "payload value: " << getContext().getPayload() << endl;
    cout << "called getContext().getPayload()" << endl;
    return 0;
}
