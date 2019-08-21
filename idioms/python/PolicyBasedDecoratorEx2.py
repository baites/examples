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


# Define policy classes

class InputMessage:
    def run(self):
        return 'hello world'

@hostclass()
class AddPrefix:
    def set_prefix(self, prefix):
        self._prefix = prefix
    def run(self):
        return self._prefix + super().run()

@hostclass()
class AddSuffix:
    def set_suffix(self, suffix):
        self._suffix = suffix
    def run(self):
        return super().run() + self._suffix

@hostclass()
class PrintOutput:
    def run(self):
        print(super().run())


PrintPrefixSuffixMessage = PrintOutput(
    AddSuffix(AddPrefix(InputMessage))
)
message = PrintPrefixSuffixMessage()
print(PrintPrefixSuffixMessage)
print(PrintPrefixSuffixMessage.__mro__)
message = PrintPrefixSuffixMessage()
message.set_prefix('Victor says: ')
message.set_suffix(' and goodbye!')
message.run()
