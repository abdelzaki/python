"""
__set__  and __reset__ descriptor
it has a problem if u used more than one instance for this method
as the same attribute would be shared   
"""


from weakref import WeakKeyDictionary


class Name:
    def __init__(self) -> None:
        self.value = 0

    def __set__(self, instance, value):
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
