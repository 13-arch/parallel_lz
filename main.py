from var_10_1 import worker_1
from var_10_2 import worker
from var_10_3 import task
from var_10_3 import main
import asyncio

async def main():
    first = worker_1()
    second = worker()
    third = await task()
    third_2= await main()

    
if __name__ == "__main__":
    asyncio.run(main()) 
