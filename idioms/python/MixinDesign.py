#! /usr/bin/env python


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

class HelloWorld:
    """Creates a host class."""
    def run(self):
        """Print message."""
        self._output('Hello world!')

class PrintHelloWorld(PrintOutput, HelloWorld):
    pass

hw = PrintHelloWorld()
hw.run() # print "Hello World!"

class SaveHelloWorld(HelloWorld, SaveOutput):
    pass

hw = SaveHelloWorld()
hw.set_filename('output.txt')
hw.run() # save "Hello World!" in output.txt
