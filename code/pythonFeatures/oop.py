# class variables
class clsA():
    name: str = "abdel"
    countery: str = "egy"
    age: int = 31

    def __init__(self) -> None:
        pass

    def printC(self):
        print(clsA.countery)

    def printObject(self):
        print(self.countery)


def clsVar():
    # access class method
    print(clsA.countery)
    clsA.countery = "egypt"
    print(clsA.countery)
    objA = clsA()
    print(objA.countery)
    objA.countery = "Äygpten"
    print(clsA.countery)
    print(objA.countery)
    objA.printC()
    objA.printObject()


# static and class method. static method does not take the class or the instance as parameter, class method takes the class as parameter
class clsStatic():
    age = 12

    def __init__(self) -> None:
        self.name: str = "clsSatic"

    @staticmethod
    def stat():
        print(" i am static")

    @classmethod
    def clsMethod(cls):
        print(cls.age)


def clsmethods():
    instance = clsStatic()
    instance.stat()
    clsStatic.stat()

    clsStatic.clsMethod()


class oper():
    def __init__(self, data) -> None:
        self.data = data

    def __add__(self, other):
        """return new instance """
        return oper(self.data + other)
    def print(self):
        print(self.data)


myInstance = oper(23)
(myInstance +2).print()

""""""
