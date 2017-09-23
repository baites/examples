#include <iostream>
#include <string>

using namespace std;

class ObjectProbe {
    unsigned counter;
public:
    ObjectProbe()
    {
        counter = 0;
        cout << "...probe contructor " << counter << endl;
    }
    ObjectProbe(const ObjectProbe & o)
    {
        counter = o.counter + 1;
        cout << "...probe copy constructor " << counter << endl;
    }
    ~ObjectProbe()
    {
        cout << "...probe destruction " << counter << endl;
        counter -= 1;
    }
    const unsigned getCounter() const
    {
        return counter;
    }
};

auto CreateContext(ObjectProbe context)
{
    return [&]() { return context; };
}

int main(int argc, const char* argv[])
{
    cout << "Creating context" << endl;
    auto context = CreateContext(ObjectProbe());
    cout << "Created context" << endl;
    cout << "Calling context().getCounter()" << endl;
    context().getCounter();
    cout << "Called context().getCounter()" << endl;
    return 0;
}
