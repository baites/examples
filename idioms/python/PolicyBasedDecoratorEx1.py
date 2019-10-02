#! /usr/bin/env python


def hostclass(*defaults):
    def decorator(host):
        def decoration(*policies):
            if len(policies) == 0:
                if len(defaults) == 0:
                    raise ValueError('No default policies available.')
                policies = defaults
            name = '{}('.format(host.__name__)
            for policy in policies[:-1]:
                name += '{},'.format(arg.__name__)
            name += '{})'.format(policies[-1].__name__)
            return type(name, (host,)+policies,{})
        return decoration
    return decorator

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

@hostclass(PrintOutput)
class HelloWorld:
    """Creates a host class."""
    def run(self):
        """Print message."""
        self._output('Hello world!')

PrintHelloWorld = HelloWorld()
print(PrintHelloWorld) # <class '__main__.HelloWorld(PrintOutput)'>
hw = PrintHelloWorld()
hw.run() # print "Hello World!"

PrintHelloWorld = HelloWorld(PrintOutput)
print(PrintHelloWorld) # <class '__main__.HelloWorld(PrintOutput)'>
hw = PrintHelloWorld()
hw.run() # print "Hello World!"

SaveHelloWorld = HelloWorld(SaveOutput)
print(SaveHelloWorld) # <class '__main__.HelloWorld(SaveOutput)'>
hw = SaveHelloWorld()
hw.set_filename('output.txt')
hw.run() # save "Hello World!" in output.txt
