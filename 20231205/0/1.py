import asyncio
from time import strftime

async def squarer(val):
    return val * val

async def doubler(val):
    return val + val

async def main():
    a = eval(input())
    b = await asyncio.gather(
            squarer(a[0]),
            squarer(a[1])
    )
    res = await asyncio.gather(
            doubler(b[0]),
            doubler(b[1])
    )
    print(res)



asyncio.run(main())