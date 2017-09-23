#include <functional>
#include <iostream>
#include <string>
#include <tuple>

using namespace std;

tuple<function<string()>, function<void(string)>> CreateMethods(string context)
{
    return {
        [&]() { return context; },
        [&](string value) { context = value; }
    };
}

int main(int argc, const char* argv[])
{
    auto [getContext, setContext] = CreateMethods("original value");
    cout << "context in orginal value: " << getContext() << endl;
    setContext("new value");
    cout << "context in new method: " << getContext() << endl;
}
