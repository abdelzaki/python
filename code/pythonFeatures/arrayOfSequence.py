

#######################
# list comprehensions:#
########################
def listComprehensions():
    # to create an array which has default values
    myArray = [int(x / 2) for x in range(5)]
    print(myArray)
    # u can create tuple inside the list also which would give 9 results
    myArray = [(char, age) for char in "abc" for age in range(3)]
    print(myArray)


########
# tuple#
########
def tuple():
    # it u can unpack the tuple
    x, y = (1, 2)
    print(x)
    # u can get the rest using *
    x, y, *r = (1, 2, 3, 4, 5, 6)
    print(r)


#############
# nametuple #
#############
def nameTuple():
    # it is a way to create tuple which u can access by name or by index
    from collections import namedtuple
    City = namedtuple('nameifCity', ['name', 'country', 'people'])
    cairo = City("ca", "Egy", 100)
    print(cairo.country)


###########################
# using * + with sequence #
###########################
def operationList():
    myarray = [1, 2, 3]
    myarry2 = [4, 5]
    myarray.append(myarry2)
    print(myarray)
    # if u want to create array inside an array
    myArray = [["_"] * 3 for _ in range(2)]
    myArray[0][2] = 12
    # dont use the short cut as it create a reference no a new array
    myArraywrongWay = [["_"]*3]*2
    myArraywrongWay[0][2] = 12
    print(myArraywrongWay)


##############
# dictionary #
##############
def dictinaryOperation():
    """key should be hashable such is tuple. while list is not hashable if u want to hash a list u 
     to use frozenset function on the set 
    """
    tt = (1, 2, 3)  # tuple is hashable
    print(hash(tt))
    # list should fail
    tlist = [1, 2, 3]
    # print(hash(tlist))
    print(hash(frozenset(tlist)))


##############
# dictionary cpmprehension#
##############
