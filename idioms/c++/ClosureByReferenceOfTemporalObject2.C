#include <cstdlib>
#include <functional>
#include <iostream>
#include <string>
#include <tuple>

using namespace std;

string genid(const int len = 10)
{
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";
    string id(len, 'x');
    for (int i = 0; i < len; ++i)
        id[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    return id;
}

class ObjectProbe {
    string id;
public:
    ObjectProbe()
    {
        id = genid();
        cout << "...probe contructor " << id << endl;
    }
    ObjectProbe(const ObjectProbe & o)
    {
        id = genid();
        cout << "...probe copy constructor " << id << " from " << o.id << endl;
    }
    ~ObjectProbe()
    {
        cout << "...probe destruction " << id << endl;
    }
    const string & getId() const
    {
        return id;
    }
};

tuple<function<ObjectProbe()>, function<void(ObjectProbe)>> CreateMethods(ObjectProbe context)
{
    return {
        [&]() { return context; },
        [&](ObjectProbe value) { context = value; }
    };
}

int main(int argc, const char* argv[])
{
    cout << "Creating context methods" << endl;
    auto [getContext, setContext] = CreateMethods(ObjectProbe());
    cout << "Created context" << endl;
    cout << "Calling getContext().getId()" << endl;
    const string & id1 = getContext().getId();
    cout << "Called getContext().getId()" << endl;
    cout << "Return id " << id1 << endl;
    cout << "Calling setContext(ObjectProbe())" << endl;
    setContext(ObjectProbe());
    cout << "Called setContext(ObjectProbe())" << endl;
    cout << "Calling getContext().getId()" << endl;
    const string & id2 = getContext().getId();
    cout << "Called getContext().getId()" << endl;
    cout << "Return id " << id2 << endl;
    return 0;
}
