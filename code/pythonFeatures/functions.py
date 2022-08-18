

##################################
# function with take n arguments #
##################################
def sum(x, y):
    return x + y


def avg(sum, first, *rest):
    """ inisde the function *rest will unpack the values,
    rest would make it a tuple 
    """
    print("rest ", rest)
    print("*rest ", *rest)
    print(sum(*rest))


################################
# function which takes k words #
################################
def makeElement(**kargs):
    for v in kargs.values():
        print(" : ", v)


###################################
# function takes *var and k words #
###################################
def funct(*kargs, **kwargs):
    # print the values
    for arg in kargs:
        print(arg)

    # print dictionary
    for kwarg in kwargs:
        print(kwarg, " : ", kwargs[kwarg])

    # print as tupe and as element
    print(kargs, " : ", *kargs)
    print(kwargs, " : ", *kwargs)


############
# callback #
############
def sum(x, y):
    return x + y


def avg(callback, element):
    print(callback(*element))


###################
# function object #
###################
def implementHelp():
    def functoinUseHelp():
        """text for help"""
        x = 1
        return 234
    thestring = functoinUseHelp.__doc__
    thestring += " asda"
    print(help(functoinUseHelp))
    print("end")


########################
# First class function #
# ######################
def firstClsMethod():
    def myfunction(n: int):
        print("hi, i am ", n)
        return n
    x = map(myfunction, [0, 1, 2])
    print(next(x))
    print(next(x))
    print(next(x))

    # myList = list(map(myfunction, range(10)))
    # print(myList)


def parameterValueAndReference():
    """list is passed by reference while tuple is by value"""
    def myfuntion(x, y):
        x += y
        print(x)
    l1 = [1, 2]
    l2 = [1, 2]
    myfuntion(l1, l2)
    print("list ", l1)
    t1 = (1, 2)
    t2 = (1, 2)
    myfuntion(t1, t2)
    print("set ", t1)

    class clsWithDefaultList():
        def __init__(self, input=[]) -> None:
            self.input = input

    obj = clsWithDefaultList()
    obj.input.append(2)
    obj2 = clsWithDefaultList()
    print("obj2 has the same value as obj because reference was created", obj2.input)


parameterValueAndReference()
