

#############################
# matching use start and end#
#############################
def startAndEnd():
    name: str = "ahmed.ger"
    print(name.startswith("a"))
    # to test end with
    print(name.endswith("ger"))
    # u can use more than one option. u have to provide tuple
    py = "x.py"
    print(py.endswith((".py", ".PY")))


######################
# search and repalce #
######################
def searchAndReplace():
    text: str = "ahmed ali zaki ahmed"
    newtext = text.replace("ahmed", "pop")
    print(newtext)


##############################
# change variable in a string#
##############################
def formatString():
    text = "hello {name} i am {age} "
    # to assign the variable in the string
    newText = text.format(name="abdel", age=31)
    print(newText)


################
# Split string #
################
def splitf():
    import re
    text: str = "ahm,ed ali zaki"
    arr = re.split('[ ,]', text)
    print(arr)


#####################
# Loop throw string #
#####################
def looping():
    for s in "ahmed":
        print(s, end=" ")
    print("")
    string: str = "my string"
    print("n" in string)
    print("str" in string)
    # index starts with 0 and 1 is included in this example, 2 is not included
    print(string[1:2])


##########
# Coding #
##########
def coding():
    # to get the binary value of the string
    print(ord("a"))
    # to get the char represenation of the integer use chr
    print(chr(115))
    # also int is avaliable
    print(int('5'), chr(ord('5') + 1))
    # to use binary to int
    print(int("11", 2))
    # to convert int to binary
    print(bin(12))


###############################
# to convert string to letter #
###############################
def formating():
    string: str = 'ahmed'
    # to convert the string to list with single char
    mylist: list[str] = list(string)
    print(mylist)
    # u can split the string according to a specific delimiter using split
    myword : str = "my name is abdel"
    print(myword.split())
    # to convert the list to string which is called on a string and takes list as argument
    mystring: str = ''.join(mylist)
    print(mystring)
    
    x :str = "i am %d live in %s" %(1,"egyot")
    print(x)
    # using template
    ex : str = "my {0} is {1}"
    ex = ex.format('s','g')
    print(ex)
    
    # u can use attribute 0.age means the attribute age in the first object
    class t():
        def __init__(self) -> None:
            self.age = 12
    obj = t()
    x : str = "my age is {0.age}".format(obj)
    print(x)

formating()
