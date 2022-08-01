

###########################################
# print only when u dont call using py -O #
###########################################
def printDebug(msg: str):

    if __debug__:
        print(msg)


printDebug("jo")
