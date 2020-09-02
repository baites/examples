#! /usr/bin/env python


from dataclasses import dataclass, FrozenInstanceError


def example_frozen_dataclass():
    """Implement example of frozen dataclass similar to class factory."""

    @dataclass(frozen=True)
    class Author:
        """Define Author type."""
        name: str
        desc: str

    author = Author(
        name='VictorB',
        desc='Engineer'
    )

    print(author.name)
    print(author.desc)
    try:
        author.desc = 'Scientist'
    except FrozenInstanceError:
        print('You cannot set this attribute (read-only).')



def example_unfrozen_dataclass():
    """Implement example of frozen dataclass similar to class factory."""

    @dataclass
    class Author:
        """Define Author type."""
        name: str
        desc: str

    author = Author(
        name='VictorB',
        desc='Engineer'
    )

    print(author.name)
    print(author.desc)
    try:
        author.desc = 'Scientist'
    except FrozenInstanceError:
        print('You cannot set this attribute (read-only).')
    print(author.desc)

example_frozen_dataclass()
print()
example_unfrozen_a_dataclass()
