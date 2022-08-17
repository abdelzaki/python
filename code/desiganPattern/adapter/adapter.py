"""
it is used to enable the user to use the same method sigbature for calling different methods
"""


class adaptee:
    def __init__(self) -> None:
        pass

    def method(self):
        print("hi i am adaptee")


class adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)


class thirdParty:
    def methodThird(self):
        print("i am third party")


class anotherThirdParty:
    def anotherMethodThird(self):
        print("i am different third")


obj = thirdParty()
objAnother = anotherThirdParty()
obj = adapter(obj, {"method": obj.methodThird})
objAnother = adapter(objAnother, {"method": objAnother.anotherMethodThird})
obj.method()
objAnother.method()
