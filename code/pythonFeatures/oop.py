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


""" Multiple inheritance """


def multpleInheritance():
    """the class on the left has higher prioirtat than the class on the right if we used multiple inheritance """
    class A:
        def ping(self):
            print("ping ", self)

    class B(A):
        def pong(self):
            print("pong B ", self)

    class C(A):
        def pong(self):
            print("PONG C", self)

    class D(B, C):
        def ping(self):
            super().ping()
            print("post-ping ", self)

        def pingpong(self):
            self.ping()
            super().ping()
            self.pong()
            super().pong()
            C.pong(self)

    d = D()
    d.pingpong()


multpleInheritance()
