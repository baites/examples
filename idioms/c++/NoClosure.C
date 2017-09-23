#include <iostream>
#include <string>

using namespace std;

string context = "original value";
string Method()
{
    return context;
}

string (*CreateMethodWithContext(string value))()
{
    context = value;
    return Method;
}

int main(int argc, const char* argv[])
{
    string (*newMethod)() = CreateMethodWithContext("new value");
    cout << "context in orginal method: " << Method() << endl;
    cout << "context in new method: " << newMethod() << endl;
    return 0;
}
