import asyncio
import time


def asyncFunction():
    """use task to create couroutine"""
    async def myfunction2():
        print("hi from 2")
        await asyncio.sleep(1)
        print("end from 2")

    async def myfunction3():
        print("hi from 3")
        await asyncio.sleep(3)
        print("end from 3")

    async def myfunction():
        print("hi")
        task1 = asyncio.create_task(myfunction2())
        task2 = asyncio.create_task(myfunction3())
        print("before await")
        await task1
        await task2
        print("end")

    asyncio.run(myfunction())
    print("i am in main")
    time.sleep(12)


def futureFunction():
    """return the value from the data using future"""
    async def fun1():
        print("func1")
        await asyncio.sleep(1)
        return 12

    async def fun2():
        print("func2")
        await asyncio.sleep(1)

    async def fun():
        task1 = asyncio.create_task(fun1())
        task2 = asyncio.create_task(fun2())
        value = await task1
        await task2
        print(value)

    asyncio.run(fun())
    print("end")


futureFunction()
