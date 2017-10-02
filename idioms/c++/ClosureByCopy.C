#include <functional>
#include <iostream>
#include <string>

using namespace std;

auto CreateClosure(const auto & context)
{
    return [context]() { return context; };
}

int main(int argc, const char* argv[])
{
    // Creating closure in with "a unmutable" object
    // where context is captured by copy or value
    auto closureA = CreateClosure("A");
    cout << "context in closureA: " << closureA() << endl;

    // Creating closure with "a mutable" object
    // where context is captured by copy or value
    string variable = "B";
    auto closureB = CreateClosure(variable);
    cout << "context in closureB: " << closureB() << endl;

    // It is NOT possible to change of the value of the context
    variable[0] = 'C';
    cout << "context in closureB: " << closureB() << endl;

    return 0;
}
