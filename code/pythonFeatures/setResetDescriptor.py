"""
descriptor is an object which implement the descriptor protocol means it has at least one of the following magic methods 
    __get__ , __set__ , __delete__ , __set__name__  
__set__  and __reset__ descriptor
it has a problem if u used more than one instance for this method
as the same attribute would be shared   
"""


from urllib.parse import non_hierarchical
from weakref import WeakKeyDictionary


class Name:
    def __init__(self) -> None:
        self.value = 0

    def __set__(self, instance, value):
        """self as it is a class, instance is the object which consumed the descriptor, owner refer to the class of this object, if descriptor 
        is called from a class then instance is None """
        self.value = value

    def __get__(self, instance, value):
        return self.value


"""
    one solution is to implement a dictioary where the key is the instance
"""


class Name2:
    def __init__(self) -> None:
        self.value = WeakKeyDictionary()

    def __set__(self, instance, value):
        self.value[instance] = value

    def __get__(self, instance, value):
        return self.value.get(instance)


class Person:
    fName = Name()
    sName = Name()
    fName2 = Name2()
    sName2 = Name2()

    def __init__(self) -> None:
        self.age = 12
        self.counter = "egy"


person = Person()
person.fName = 1
person.sName = 2
person.fName2 = 1
person.sName2 = 2

person2 = Person()
person2.fName = 21
person2.sName = 22
person2.fName2 = 21
person2.sName2 = 22

print(" fName ", person.fName)
print(" sName ", person.sName)
print(" fName2 ", person2.fName)
print(" sName2 ", person2.sName)

print("-------------")
print(" fName ", person.fName2)
print(" sName ", person.sName2)
print(" fName2 ", person2.fName2)
print(" sName2 ", person2.sName2)


def callOnClass():
    """
    descriptor can be called from the class and from the instacne of the class
    """

    class DescriptorCls:
        def __get__(self, instance, owner):
            """self refere to the descriptor"""
            if instance is not None:
                print("called on instance ", instance)
            else:
                print("called on class ", owner)

    class DescriptorClient():
        DescriptorAttr = DescriptorCls()

    DescriptorClient.DescriptorAttr
    DescriptorClient().DescriptorAttr


class NameWithDict():
    """ using name for the descriptor"""

    def __init__(self, name) -> None:
        self.name = name

    def __set__(self, instance, value):
        self.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is not None:
            return self.__dict__[self.name]

class User():
    descriptor = NameWithDict("value")
    
user1 = User()
user1.descriptor = "ali"
user2 = User()
user2.descriptor = "abdel"

print(user1.descriptor)
print(user2.descriptor)


