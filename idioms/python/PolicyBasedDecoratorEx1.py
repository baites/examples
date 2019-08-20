#! /usr/bin/env python


def hostclass(host):
    def wrapper(*policies):
        name = '{}('.format(host.__name__)
        for policy in policies[:-1]:
            name += '{},'.format(arg.__name__)
        name += '{})'.format(policies[-1].__name__)
        return type(name, (host,)+policies,{})
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


@hostclass
class HelloWorld:
    """Creates a host class."""
    def run(self):
        """Print message."""
        self._output('Hello world!')


PrintHelloWorld = HelloWorld(PrintOutput)

print(PrintHelloWorld)

hw = PrintHelloWorld()
hw.run() # print "Hello World!"

SaveHelloWorld = HelloWorld(SaveOutput)

hw = SaveHelloWorld()
hw.set_filename('output.txt')
hw.run() # save "Hello World!" in output.txt
