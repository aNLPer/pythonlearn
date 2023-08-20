import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
   task1 = asyncio.create_task(say_after(1, "Bob"))
   task2 = asyncio.create_task(say_after(2, "welch"))
   print(f"start at {time.time()}")
   await task1
   await task2
   print(f"end at {time.time()}")

asyncio.run(main())