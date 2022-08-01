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
    for k, v in xydict.items():
        print(k, " -> ", v)


dictf()
