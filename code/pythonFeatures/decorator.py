"""
Decorator is a function which takes a function as argument and return another a new one as output which is defined in the function
"""
print(__debug__)


def outerFunction(func):
    """outter function """
    print("function in outer function")

    def innerFunc(*kargs, **kwargs):
        print("inside inner")
        func(*kargs, **kwargs)
        print("after")

    return innerFunc


@outerFunction
def func(x):
    print("the function")
    print(x)


################
# enable debug #
################

def printDebug(msg: str):
    
    if __debug__:
        print(msg)
   
printDebug("jo")

