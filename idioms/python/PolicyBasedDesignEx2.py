#! /usr/bin/env python

# Define possible dependencies

def PrintOutput(message):
    """Implement output dependency."""
    print(message)

def EnglishLanguage():
    """Implement english message."""
    return 'Hello world!'

def FinnishLanguage():
    """Implement english message."""
    return 'Hei maailma!'

# Define class depend on the dependencies

class HelloWorld:
    """Implements HelloWorld using DI."""
    def __init__(self, message, output=PrintOutput):
        """Constructor."""
        self._message = message
        self._output = output

    def run(self):
        """Run HelloWorld."""
        self._output(self._message())

hw = HelloWorld(EnglishLanguage)
hw.run() # prints "Hello World!"

hw = HelloWorld(FinnishLanguage)
hw.run() # prints "Hei maailma!"
