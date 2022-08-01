

#############################
# to enable print on object #
#############################
class pair():
    def __init__(self) -> None:
        self.x = 1
        self.y = 2

    def __repr__(self) -> str:
        # return "hi {0.x}".format(self)
        return " hi %r" % (self.x)

#############
# properity #
#############


class Person():
    def __init__(self) -> None:
        self.firstName = "default"
    # getter

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value


person = Person()
print(person.firstName)

person.firstName = "ahmed"
print(person.firstName)
person.firstName = "3"
print(person.firstName)
