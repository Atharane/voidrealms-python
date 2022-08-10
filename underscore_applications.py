# Single underscore '_'
# Skipping, the variable is not referenced, but is just used as a placeholder
for _ in range(5):
    print('*')


# Underscores in Python Classes

class Base:
    # Weak Private/ Protected
    _attr_a = ''

    def set_a(self, name):
        self._attr_a = name
        print(f'weak private a: {self._attr_a}')

    # Strong Private
    @staticmethod
    def __method_b():
        print('strong private method __method_b')

    def c(self):
        self.__method_b()

    # Before and After
    def __init__(self):
        pass

    def __method_e__(self):
        pass


class Derived(Base):
    def method_d(self):
        self.__method_b()  # trying to access private method outside the scope of the class not permitted


# Before (Single)
# Internal use only, called a weak private
p = Base()
p.set_a('x')  # ideal way to set/modify protected data members
p._attr_a = 'y'  # permissible yet not advisable

# Before (Double)
# Internal use only, avoid conflict in subclass
# and tells python to rewrite the name (Mangling)
p = Base()
p.c()
# p.__method_b()  # trying to access private member outside the scope of the class thus not permitted

c = Derived()
# c.method_d()  # method_d is a method which tries to call private method from derived class thus not permitted

# After (Any)
# Helps to avoid naming conflicts with keywords
class_ = Base()
print(class_)

# Before and after
# Considered special to Python, like the init and main function
p = Base()
p.__method_e__()
