import heapq


###################################
# get smallest and largest numbers#
###################################
def nlarge():
    # if u want to get the smallest and the largest numbers in list
    nums = [1, 2, 3, 10, 20, 30, -1]
    nlarge = heapq.nlargest(3, nums)
    print(nlarge)
    nsmallest = heapq.nsmallest(1, nums)
    print(nsmallest)


#############################
# Dictionary with order keys#
#############################
def orderDictionary():
    from collections import OrderedDict
    od = OrderedDict()
    od["a"] = 100
    od["b"] = 1
    for k, v in od.items():
        print(k, " : ", v)
    

    d = dict()
    d["b"] = 100
    d["a"] = 1
    for k, v in d.items():
        print(k, " : ", v)



orderDictionary()