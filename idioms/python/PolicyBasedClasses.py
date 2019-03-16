#! /usr/bin/env python


# Class is define but policy is undefined
# Class (no object) instantion deferred

def PolicyBasedClass(policy):
    """Creates a policy based class."""
    class _(policy):
        """Implements class affected by the policy."""
        def __init__(self):
            self.value = None

        def set(self, value):
            self.value = value
            return self.value
    return _

# Policy defintions

class AddConstantPolicy:
    """Implement add constant policy."""
    def get(self):
        """Define get interface that add 10 to value"""
        return self.value + 10

class MultiplyConstantPolicy:
    """Implement multiply constant policy."""
    def get(self):
        """Policy ."""
        return self.value * 10

# Class instantation customized by policy
AddConstantClass = PolicyBasedClass(
    policy = AddConstantPolicy
)

# Object instantation
o = AddConstantClass()
o.set(5)
print(o.get())

# Class instantation customized by policy
MultiplyConstantClass = PolicyBasedClass(
    policy = MultiplyConstantPolicy
)

# Object instantation
o = MultiplyConstantClass()
o.set(5)
print(o.get())
