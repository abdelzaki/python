

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
    text:str = "ahm,ed ali zaki"
    arr =  re.split('[ ,]',text)
    print(arr)
splitf()