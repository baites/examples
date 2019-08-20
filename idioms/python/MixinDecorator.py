#! /usr/bin/env python


def mixinbase(baseclass):
    def wrapper(*mixins):
        name = '{}('.format(baseclass.__name__)
        for mixin in mixins[:-1]:
            name += '{},'.format(mixin.__name__)
        name += '{})'.format(mixins[-1].__name__)
        return type(name, mixins+(baseclass,), {})
    return wrapper


class PrintOutput:
    """Implement print output mixin."""
    def _output(self, message):
        print(message)

class SaveOutput:
    """Implement save output mixin."""
    def set_filename(self, filename):
        self.filename = filename
    def _output(self, message):
        with open(self.filename, 'w') as file:
            file.write(message)

@mixinbase
class HelloWorld:
    """Creates a host class."""
    def run(self):
        """Print message."""
        self._output('Hello world!')


PrintHelloWorld = HelloWorld(PrintOutput)

print(PrintHelloWorld)
print(PrintHelloWorld.__mro__)


hw = PrintHelloWorld()
hw.run() # print "Hello World!"

SaveHelloWorld = HelloWorld(SaveOutput)

hw = SaveHelloWorld()
hw.set_filename('output.txt')
hw.run() # save "Hello World!" in output.txt
