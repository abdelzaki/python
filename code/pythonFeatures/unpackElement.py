import struct


def usingStruct():
    sequenceCounter = 34
    protocolVersion = 0x0100
    msgType = 0x5064
    comId = 0
    etbTopoCnt = 0
    opTrnTopoCnt = 0
    datasetLength = 0
    reserved01 = 0
    replayComId = 0
    replayIpAddress = 0

    data = struct.pack(">IHHIIIIIII",
                       sequenceCounter,
                       protocolVersion,
                       msgType,
                       comId,
                       etbTopoCnt,
                       opTrnTopoCnt,
                       datasetLength,
                       reserved01,
                       replayComId,
                       replayIpAddress)
    data2, = struct.unpack(">I", data[0: 4])
    print(data2)


def throwUnusedData():
    mylist = [1, 2, 3, [1, 2, 3]]
    _, two, three, anotherlist = mylist
    print(anotherlist)


def usingList():
    """u can element using * to catch everything"""
    grades = [[1, 2, 5], [10, 20, 50]]
    for grade in grades:
        f, *middle, l = grade
        print(f)
        print(middle)
        print(l)


def starToFowared():
    records = [("2", 1, 2), ("3", 1, 2, 3)]

    def getTwo(one, two):
        print(one, " ", two)

    def getThree(one, two, three):
        print(one, " ", two, " ", three)

    for tag, *element in records:
        if tag == "2":
            getTwo(*element)
        if tag == "3":
            getThree(*element)


starToFowared()
