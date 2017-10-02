#include <functional>
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

template<typename T>
auto CreateClosure(const auto & value)
{
    T context = value;
    return [&context]() { return context; };
}

int main(int argc, const char* argv[])
{
    // Creating closure using a lifetime probe object
    // where context is captured by reference
    auto closureA = CreateClosure<LifetimeProbe>(LifetimeProbe());
    cout << "context in closureA payload: " << closureA().getPayload() << endl;

    // Creating closure in with "a unmutable" object
    // where context is captured by reference
    auto closureB = CreateClosure<string>("A");
    cout << "context in closureB: " << closureB() << endl;

    return 0;
}
