

###############
# empty bytes #
###############
def basic():
    emptyBytes = bytes(4)  # create 4 bytes
    print(emptyBytes)
    print(type(emptyBytes))

    # to pass value to the byte which is immutable
    data_byte = bytes(b'\xFF\xFF')
    print(data_byte)

    # to pass list
    data_byte = bytes([1, 2, 3, 255])
    print(data_byte)

    # to convert from string to bytes
    data_bytes = bytes("hi", "ascii")
    print("asci ", data_bytes)

    # for  mutable bytes use byte array
    mutable_byte = bytearray(b"\xFE\xFF")
    print(mutable_byte)
    mutable_byte.append(255)
    print(mutable_byte)
    for val in mutable_byte:
        print(val)


####################
# Code and decode  #
###################
def codeDecode():
    # to get the ascii code of a character
    print("ord('A') ", ord("A"))
    print("ord('A') ", format(ord("A"), 'x'))
    # to create byes form hex
    print(bytes.fromhex("Af"))
    print(bytes(b"\xAf"))
    # to conver string to hex
    print(bytes("AB", "ascii").hex())
    # to loop throw bytes
    data = bytes(b"\xAf\01")
    print(hex((data[0] & 0xf0)>>4))
codeDecode()
