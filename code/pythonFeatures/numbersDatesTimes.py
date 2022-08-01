
############
# rounding #
############
def rounding():
    i: int = 1.234
    print(round(i, 1))

    # u can round tens. hundered, thousands, etc
    bigI: int = 12359
    print(round(bigI, -2))


#####################
#woring with binary #
#####################
def binf():
    x: int = 1234
    xb = bin(x)
    print(xb)
    # to get the number as hex
    print(hex(x))
    # if u want to get ride of the start of the data use format
    print(format(x, 'b'))
    # to get the hex value
    print(format(x, 'x'))


########################
# to work with maximal #
########################
def maxNumbers():
    x: float = float("inf")
    y: float = float("-inf")
    print(x > 2344)



##########
# random #
##########
def randomf():
    import random
    values = [i for i in range(5)]
    print((random.choice(values)))
    print((random.choice(values)))
    print((random.choice(values)))
    # to get a sample from a data
    print(random.sample(values,2))
    print(random.sample(values,2))
    # to shulffe the values
    random.shuffle(values)
    print(values)
    # to produce a random integer
    print(random.randint(0,10))

randomf()