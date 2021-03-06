#! /usr/bin/env python
"""Implement an example of a base class factory function."""


def CreateClass(name, fields, parents=(), frozen=False):
    """Create a base class with a given fields and parents."""

    def getter(field):
        return lambda self: getattr(self, '_{}'.format(field))

    def setter(field):
        return lambda self, value: setattr(self, '_{}'.format(field), value)

    def deleter(field):
        return lambda self: delattr(self, '_{}'.format(field))

    def init(self, **kwargs):
        for field in fields:
            if field not in kwargs:
                raise ValueError(
                    'Missing initial value for argument "{}"'.format(field)
                )
            setattr(self, '_{}'.format(field), kwargs[field])

    members = {'__init__': init}
    for field in fields:
        if frozen:
            members[field] = property(
                getter(field)
            )
        else:
            members[field] = property(
                getter(field),
                setter(field),
                deleter(field)
            )

    globals()[name] = type(name, parents, members)
    return globals()[name]


def example_frozen_class():
    """Implement example of frozen class."""

    CreateClass('Author', (
        'name',
        'desc'
    ), frozen=True)

    author = Author(
        name='VictorB',
        desc='Engineer'
    )

    print(author.name)
    print(author.desc)
    try:
        author.desc = 'Scientist'
    except AttributeError:
        print('You cannot set this attribute (read-only).')


def example_unfrozen_class():
    """Implement example of unfrozen class."""

    CreateClass('Author', (
        'name',
        'desc'
    ))

    author = Author(
        name='VictorB',
        desc='Engineer'
    )

    print(author.name)
    print(author.desc)
    author.desc = 'Scientist'
    print(author.desc)


example_frozen_class()
print()
example_unfrozen_class()
