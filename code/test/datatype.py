from collections import defaultdict

"""
#######################################
##############  list  #################
#######################################
"""

def listOperation():
    list1 = [1]
    list2 = [100]
    print("Extend two lists")
    list1And2 = list1 + list2
    print(list1And2)
    print("Append to a list")
    list1.append(2)
    print(list1)
    print("Get element according to an index ")
    print(list1[1])
    print("Remove an element ")
    print("Remove an element ", list1.remove(1), " ", list1)
    print("List with initial values ")
    list3 = [0] * 26
    print(list3)
    print("List with values ")
    freq = [i for i in range(5)]
    print(freq)
    print(list3)
    print("Append to an empty list ")
    list4 = []
    list4.append(1)
    list4.append(2)
    print(list4)
    print("Get the index of an element")
    print(list4.index(2))
    print("To copy a list ")
    list5 = list4[0:1]
    print(list5)

"""
#######################################
############  Dictionary  #############
#######################################
"""
def dictionaryOperation():

    dictionary = {}  # Declare an dictionary
    print("Add an item to the dictionaty")
    dictionary["key1"] = "value1"
    dictionary["key2"] = "value2"
    print(dictionary)
    print("Access key which does not exist ")
    print(dictionary.get("key3", False))
    print("Rewrite an element")
    dictionary["key1"] = 12
    print(dictionary)
    print("List inside dicionary")
    dictionary2 = defaultdict(list)
    dictionary2["key1"].append("1")
    dictionary2["key1"].append("2")
    dictionary2["key2"].append("3")
    print(dictionary2)
    print("Dictonary inside dictionary")
    dictionary3 = defaultdict(dict)
    dictionary3["key1"]["key11"] = "value111"
    print(dictionary3)

    print(
        "list inside Dictonary inside dictionary { key1 = { key11 = [] , key12 = []}, { key2 = { key21 = [] }} ")
    dictionary4 = defaultdict(lambda: defaultdict(list))
    dictionary4["key1"]["key11"].append("value1")
    dictionary4["key1"]["key12"].append("value2")
    dictionary4["key2"]["key12"].append("value2")
    dictionary4["key2"]["key12"].append("value22")
    print(dictionary4)
    print("Loop throw elements")
    for key1, dict1 in dictionary4.items():
        for key2, listelements in dict1.items():
            for element in listelements:
                print(element)

"""
#################################
############  set  1#############
#################################
"""
def setOperation():
    print("To add an element in the set")
    set1 = set()
    print("set.add(1)", set1.add(1))
    print("To check if an element exist in the set")
    if 1 in set1:
        print("if 1 in set1", set1)
   
def algorithum():
    list1 = [1,4,0,12,2,100,5]
    print("To sort algorithum")
    list2 = sorted(list1)
    print("sorted(list1) " , list2)
    print("To iterate with index and value")
    for i, val in enumerate(list1):
        print(i," : ", val)
algorithum()
