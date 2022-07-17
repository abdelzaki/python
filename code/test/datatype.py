"""
#######################################
##############  list  #################
#######################################
"""


from collections import defaultdict
#from typing import DefaultDict


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
    print("Append to an empty list ")
    list4 = []
    list4.append(1)
    print(list4)


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


dictionaryOperation()
