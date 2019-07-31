#! /usr/bin/env python

# Define policy classes

class PrintOutput:
    """Implement output policy."""
    def _output(self, message):
        print(message)

class SaveOutput:
    """Implement save output policy."""
    def set_filename(self, filename):
        self.filename = filename

    def _output(self, message):
        with open(self.filename, 'w') as file:
            file.write(message)

class EnglishLanguage:
    """Implement english message."""
    def _message(self):
        """Return message"""
        return 'Hello world!'

class FinnishLanguage:
    """Implement english message."""
    def _message(self):
        """Return message"""
        return 'Hei maailma!'

# Define host class

def HelloWorld(language, output=PrintOutput):
    """Creates a host class."""
    class _(language, output):
        """Implements class affected by the policy."""
        def run(self):
            """Print message."""
            self._output(self._message())
    return _

HelloWorldEnglish = HelloWorld(EnglishLanguage)
hw = HelloWorldEnglish()
hw.run()

HelloWorldFinnish = HelloWorld(FinnishLanguage)
hw = HelloWorldFinnish()
hw.run()

HelloWorldEnglish = HelloWorld(
    language=EnglishLanguage,
    output=SaveOutput
)
hw = HelloWorldEnglish()
hw.set_filename('output.txt')
hw.run() # save "Hello World!" in output.txt
