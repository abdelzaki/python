

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


############
# callback #
############
def sum(x, y):
    return x + y


def avg(callback, element):
    print(callback(*element))


avg(callback=sum, element=(1, 2))
