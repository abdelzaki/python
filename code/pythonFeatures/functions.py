

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
    print(kargs, " : " ,*kargs)
    print(kwargs, " : " ,*kwargs)

funct(1,2,3, type=12, age=14)

############
# callback #
############
def sum(x, y):
    return x + y


def avg(callback, element):
    print(callback(*element))
