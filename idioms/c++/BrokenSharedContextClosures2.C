#include <cstdlib>
#include <functional>
#include <iostream>
#include <memory>
#include <string>
#include <tuple>

using namespace std;

template<typename T>
class LifetimeProbe {
    T payload;
public:
    LifetimeProbe(const T & value)
    {
        cout << "...probe constructor " << &(*this) << endl;
        payload = T(value);
    }
    LifetimeProbe(const LifetimeProbe & o)
    {
        cout << "...probe copy constructor " << &(*this) << " from " << &o << endl;
        payload = o.payload;
    }
    ~LifetimeProbe()
    {
        cout << "...probe destruction " << &(*this) << endl;
    }
    const T & getPayload() const
    {
        return payload;
    }
};

template<typename T>
tuple<function<T()>, function<void(T)>> CreateMethods(const T & value)
{
    T context = value;
    return {
        [&]() { return context; },
        [&](T value) { context = value; }
    };
}

int main(int argc, const char* argv[])
{
    cout << "creating context methods with LifetimeProbe<string>(\"A\")" << endl;
    auto [getContext, setContext] = CreateMethods(
        LifetimeProbe<string>("A")
    );
    cout << "created context" << endl;
    cout << "calling getContext().getPayload()" << endl;
    auto payload = getContext().getPayload();
    cout << "payload value: " << payload << endl;
    cout << "called getContext().getPayload()" << endl;
    cout << "calling setContext(LifetimeProbe<string>(\"B\"))" << endl;
    setContext(LifetimeProbe<string>("B"));
    cout << "called setContext(LifetimeProbe<string>(\"B\"))" << endl;
    cout << "calling getContext().getPayload()" << endl;
    payload = getContext().getPayload();
    cout << "payload value: " << payload << endl;
    cout << "called getContext().getPayload()" << endl;
    return 0;
}
