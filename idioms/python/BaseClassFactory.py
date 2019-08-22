
def BaseClass(name, fields, parents=()):
    
    def property_getter(field):
        def getter(self):
            return getattr(self, '_{}'.format(field))
        return getter

    def init(self, **kwargs):
        for field in fields:
            if field not in kwargs:
                raise ValueError(
                    'Missing initial value for argument "{}"'.format(field)
                )
            setattr(self, '_{}'.format(field), kwargs[field])

    dict = { '__init__': init }
    for field in fields:
        dict[field] = property(
            property_getter(field)
        )

    globals()[name] = type(name, parents, dict)
    return type(name, parents, dict)


BaseClass('AuthorBase',(
    'name',
    'desc'
))

class Author(AuthorBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @AuthorBase.name.setter
    def name(self, value):
        self._name = value

print(Author.__mro__)

author = Author(
    name = 'VictorB',
    desc = 'Programmer'
)

print(author.name)
print(author.desc)
author.name = 'Vic'
print(author.name)
