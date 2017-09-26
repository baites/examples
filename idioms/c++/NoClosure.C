#include <iostream>
#include <string>

using namespace std;

// Defining context and method in global namespace.
string context = "A";
string Method()
{
    return context;
}

// Return a reference to Method.
string (*CreateMethodWithContext(string value))()
{
    context = value;
    return Method;
}

int main(int argc, const char* argv[])
{
    // Print default initial context value
    cout << "context when calling Method(): " << Method() << endl;

    // Create a reference to method and set context
    string (*method)() = CreateMethodWithContext("B");
    cout << "context when calling method: " << method() << endl;
    return 0;
}
