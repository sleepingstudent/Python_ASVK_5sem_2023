import asyncio

async def snd(evsnd):
    evsnd.set()
    print("snd: generated <evsnd>")
    #print('waiting for it ...')
    #await event.wait()
    #print('... got it!')

async def mid1(evsnd, evmid1):
    await evsnd.wait()
    print("mid1: received <evsnd>")
    evmid1.set()
    print("mid1: generated <evmid1>")

async def mid2(evsnd, evmid2):
    await evsnd.wait()
    print("mid2: received <evsnd>")
    evmid2.set()
    print("mid2: generated <evmid2>")

async def rcv(evmid1, evmid2):
    await asyncio.gather(
            evmid1.wait(),
            evmid2.wait()
    )
    print("rcv: received <evmid1>" + "rcv: received <evmid2>")
'''    await evmid1.wait()
    print("rcv: received <evmid1>")
    await evmid2.wait()
    print("rcv: received <evmid2>")'''



async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    # Create an Event object.
    evsnd = asyncio.Event()
    evmid1 = asyncio.Event()
    evmid2 = asyncio.Event()
    res = await asyncio.gather(
            snd(evsnd),
            mid1(evsnd, evmid1),
            mid2(evsnd, evmid2),
            rcv(evmid1, evmid2)
    )
    '''task1 = asyncio.create_task(snd(evsnd))
    task2 = asyncio.create_task(mid1(evsnd, evmid1))
    task3 = asyncio.create_task(mid2(evsnd, evmid2))
    task4 = asyncio.create_task(rcv(evmid1, evmid2))
    await task1
    await task2
    await task3
    await task4'''
    # Spawn a Task to wait until 'event' is set.
    #waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    #await asyncio.sleep(1)
    #event.set()

    # Wait until the waiter task is finished.
    #await waiter_task

asyncio.run(main())