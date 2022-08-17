
# it is used to force implement len and getitem
from collections.abc import Sequence
from typing import List


def sequence():
    class Items(Sequence):
        """class which implement sequence """

        def __init__(self, *values) -> None:
            super().__init__()
            self._values = list(values)

        def __len__(self):
            return len(self._values)

        def __getitem__(self, item):
            return self._values.__getitem__(item)

    item = Items(1, 2, 3)
    print(len(item))
    print(item[0])


def privateMethod():
    """Donot use this a way because it is not the standard. Python create an alias to the attribute by adding the name of the class to the method """
    class PrivateCls():
        def __init__(self) -> None:
            self.__private = 12

    privateObj = PrivateCls()
    print(privateObj._PrivateCls__private)
    # use .__dict__ to get to know what is accessible to you
    print(privateObj.__dict__)


def iterableFunction():
    """Iterable -> means it implements  __iter__  and u can call for loop on it. it should return object which implement next 
        iterator -> object with a state and implement next method and goes only forward   
    """
    nums: List[int] = [
        1, 3, 5, 7, 9]  # it is iterable means u can call iter on it which will return iterator
    # this would return iterator which u cal call next on it
    i_nums = iter(nums)
    print(i_nums)
    print(next(i_nums))
    print(next(i_nums))
    print(next(i_nums))
    print("iteraor class")

    class iteratorCls():
        def __init__(self, str, stp) -> None:
            self.str, self.stp = str, stp

        def __iter__(self):
            """implement iterable """
            print("iter")
            return self

        def __next__(self):
            """implement iterator"""
            if self.str > self.stp:
                raise StopIteration()
            curr = self.str
            self.str += 1
            return curr

    iteratorObj = iteratorCls(1, 5)
    for i in iteratorObj:
        print(i)


def containerFunction():
    """object which implement __contains__ ex element in container which would call container.__contains__(element)"""
    class Container():
        def __contains__(self, element) -> bool:
            return True if element < 10 else False

    container = Container()
    print(10 in container)
    print(1 in container)


containerFunction()
