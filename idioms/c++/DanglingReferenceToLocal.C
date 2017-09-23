#include <cstdlib>
#include <iostream>
#include <string>

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
        cout << "...probe constructor " << id << endl;
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

const ObjectProbe & CreateLocalProve()
{
    ObjectProbe probe;
    return probe;
}

int main(int argc, const char* argv[])
{
    cout << "Creating local probe" << endl;
    const ObjectProbe & probe = CreateLocalProve();
    cout << "Created local probe" << endl;
    cout << "Calling probe.getId()" << endl;
    const string & id = probe.getId();
    cout << "Called probe.getId()" << endl;
    cout << "Return id " << probe.getId() << endl;
    return 0;
}
