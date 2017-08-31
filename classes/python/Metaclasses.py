class MetaType(type):
    def __init__(cls, *args, **kwargs):
        print('__init__')
        return super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('__call__')
        return super().__call__(*args, **kwargs)

class A(metaclass=MetaType):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'A:{}'.format(self.val)

a = A('hola')
b = A('chau')
print(a)
print(b)
