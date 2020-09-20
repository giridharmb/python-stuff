import asyncio
import random

async def exec(name, sleep):
    print("Inside : {} , sleep-time : {}".format(name, sleep))
    await asyncio.sleep(sleep)
    print("Done with {}".format(name))
    return random.randint(0,10)

async def main():
    func1 = loop.create_task(exec("doStuff1", 6))
    func2 = loop.create_task(exec("doStuff2", 2))
    func3 = loop.create_task(exec("doStuff3", 4))

    await asyncio.wait([func1,func2,func3])

    return func1, func2, func3

if __name__ == "__main__":
    try:
        
        loop = asyncio.get_event_loop()
        
        f1, f2, f3 = loop.run_until_complete(main())
        
        print(f1.result())
        print(f2.result())
        print(f3.result())

        print("DONE WIH ALL")

    except Exception as ex:
        print("Error : {}".format(ex))
    finally:
        loop.close()