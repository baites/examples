#include <functional>
#include <iostream>
#include <string>

using namespace std;

auto CreateMethodWithContext(string value)
{
    string context = value;
    return [&]() {
        return context;
    };
}

int main(int argc, const char* argv[])
{
    auto origMethod = CreateMethodWithContext("original value");
    auto newMethod = CreateMethodWithContext("new value");
    cout << "context in orginal method: " << origMethod() << endl;
    cout << "context in new method: " << newMethod() << endl;
}
