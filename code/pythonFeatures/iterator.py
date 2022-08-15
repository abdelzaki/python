def iterF():
    items = [1, 2, 3]
    it = iter(items)
    print(next(it))
    print("--")
    print(next(it))


########################
# class with iteration #
########################
def iterClass():
    """if u want to enable for loop on a class """
    class Node:
        def __init__(self) -> None:
            self.mylist = [1, 2, 3, 4]

        def __iter__(self):
            return iter(self.mylist)

    node = Node()
    for n in node:
        print(n)


##########################
# Iterator over two data #
##########################
def ziff():
    xpts = [1, 2, 3]
    ypts = [10, 20, 30]
    for x, y in zip(xpts, ypts):
        print(x,  " : ", y)


############################
# create dictionary or list#
############################
def dictf():
    xpts = [1, 2, 3]
    ypts = [10, 20, 30]
    xydict = dict(zip(xpts, ypts))
    xylist = list(zip(xpts, ypts))
    print(xylist)
    print(xydict)

    for k, v in xydict.items():
        print(k, " -> ", v)


def getMinMaxfromDict():
    """get the min and max according to the key """
    mydict = {1: "a", 2: "b", 3: "c"}
    print(min(mydict.keys()))
    # according to the key
    print(min(zip(mydict.keys(), mydict.values()))[1])


def filterElements():
    input = [1, 2, 3, "a", "b"]

    def myfilterFunction(element):
        try:
            x = int(element)
            return True
        except:
            return False

    result = list(filter(myfilterFunction, input))
    print(result)


def chain():
    from collections import ChainMap
    fdict = {"1": 1, "2": 2}
    sdict = {"3": 3, "2": 4}
    mydict = ChainMap(fdict, sdict)
    print(mydict)
    print(mydict["2"])


chain()
