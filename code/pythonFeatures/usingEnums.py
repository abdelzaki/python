"""Enum it is used to make compare easier"""
from enum import Enum, IntEnum

# Enum does not support compare only == is supported.
Size = Enum("Size", "s m l")
mySize = Size.s
yourSize = Size.m

print(mySize == yourSize)
anotherSize: Size = Size.l
print(anotherSize)

# it supports compare as it can be casted to integer
IntSize = IntEnum("IntSize", "s m l")

myIntSize = IntSize.s
yourIntSize = IntSize.m

print(myIntSize < yourIntSize)
