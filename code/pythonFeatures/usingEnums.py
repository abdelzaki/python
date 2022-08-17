"""Enum it is used to make compare easier"""
from enum import Enum, IntEnum
Size = Enum("Size", "s m l")
mySize = Size.s
yourSize = Size.m

print(mySize == yourSize)
anotherSize : Size  = Size.l
print(anotherSize)

IntSize = IntEnum("IntSize", "s m l")

myIntSize = IntSize.s
yourIntSize = IntSize.m

print(myIntSize < yourIntSize )
