#! /usr/bin/env python

# Define policy classes

class InputMessage:
    """Implement a message."""
    def run(self):
        return 'hello world'

def AddPrefix(Input):
    """Implement the concatenation of a prefix."""
    class _(Input):
        def set_prefix(self, prefix):
            self._prefix = prefix
        def run(self):
            return self._prefix + super().run()
    return _

def AddSuffix(Input):
    """Implement the concatenation of a suffix."""
    class _(Input):
        def set_suffix(self, suffix):
            self._suffix = suffix
        def run(self):
            return super().run() + self._suffix
    return _

def PrintOutput(Input):
    """Print message as output."""
    class _(Input):
        def run(self):
            print(super().run())
    return _

PrefixMessage = AddPrefix(InputMessage)
PrintPrefixSuffixMessage = PrintOutput(
    AddSuffix(AddPrefix(InputMessage))
)
message = PrintPrefixSuffixMessage()
message.set_prefix('Victor says: ')
message.set_suffix(' and goodbye!')
message.run()
