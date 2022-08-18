# type would return the class of the object
"""
python types are
bool, int, float, complex, bytes, str, function, class
"""

"""
Meta class:
Sequence should implement __len__ and __getitem__
    __getitem__ -> enable indexing

"""


#import abc   # ABC means abstack base class
import collections.abc
x = 1
print(type(x))


def differentBetweenIsAndEqual():
    """There is a differnece between is and == """
    x = {"name": "abdel"}
    y = x
    print(x == y,  x is y)
    z = {"name": "abdel"}
    print(x == z,  x is z, id(x), id(y), id(z))


def abstractMethod():

    class base(abc.ABC):
        @abc.abstractmethod
        def implement(self):
            """"""

        def hi(self):
            print("hi")

    class subclass(base):
        def __init__(self) -> None:
            super().__init__()

        def implement(self):
            pass

    subobj = subclass()

##################################################
# __getitem__ enables u to pass [] to the object #
##################################################


def enableIndexing():
    class MySeq:
        def __getitem__(self, index):
            return index

    s = MySeq()
    print(s[1:4])  # where it would converted to slice(1,4,None)


def duckTyping():
    """ - If is has the same method then u can use it exchangable
        - U are allowed to use isinstance only on abstract class
    """

    class Duck():
        def quack(self):
            print("quack from Duck")

    class Person():
        def quack(self):
            print("quack from Person")

    def method(thing):
        thing.quack()

    duck = Duck()
    person = Person()

    method(duck)
    method(person)

    class Items():
        """class which implement sequence """

        def __init__(self, *values) -> None:
            self._values = list(values)

        def __len__(self):
            return len(self._values)

        def __getitem__(self, item):
            return self._values.__getitem__(item)

    item = Items()
    print("Is instance ",isinstance(Items(), collections.abc.Sequence))


duckTyping()
