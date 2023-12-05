import asyncio
import time


async def prod(q1, kill=None):
    cnt = 0
    while True:
        await q1.put(f"value {cnt}")
        print(f"prod1:put {cnt} to q1")
        await asyncio.sleep(1)
        cnt += 1
        if cnt == 5:
            break
    await q1.put(kill)

async def mid(q1, q2, kill=None):
    while True:
        val = await q1.get()
        print(f"mid:got {val} from q1")
        await q2.put(f"value {val}")
        print(f"mid:put {val} to q2")

async def cons(q2, kill=None):
    while True:
        val = await q2.get()
        print(f"cons:got {val} from q2")

'''
async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')'''


async def main():
    # Create a queue that we will use to store our "workload".
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()


    res = await asyncio.gather(
            prod(q1),
            mid(q1, q2),
            cons(q2)
    )

asyncio.run(main())