import httpx
import requests
from time import perf_counter
import asyncio

URL = "https://quotable.io/random"

def requests_for_loop(number_of_request: int = 50):
    """Classic for loop with get request."""
    start = perf_counter()

    for i in range(number_of_request):
        res = requests.get(URL)
        print(i, res.json()["author"])

    end = perf_counter()
    print("Requests FOR LOOP -> Time: ", end - start) 


def requests_for_loop_client_sync(number_of_request: int = 50):
    """For loop with Session."""
    start = perf_counter()
    
    with requests.Session() as session:
        for i in range(number_of_request):
            res = session.get(URL)
            print(i, res.json()["author"])
    
    end = perf_counter()
    print("FOR LOOP CLIENT -> Time: ", end - start)


def httpx_for_loop(number_of_request: int = 50):
    """Classic for loop with get request."""
    start = perf_counter()

    for i in range(number_of_request):
        res = httpx.get(URL)
        print(i, res.json()["author"])

    end = perf_counter()
    print("Httpx FOR LOOP -> Time: ", end - start)    


def httpx_for_loop_client_sync(number_of_request: int = 50):
    """For loop with Client session."""
    start = perf_counter()
    
    with httpx.Client() as client:
        for i in range(number_of_request):
            res = client.get(URL)
            print(i, res.json()["author"])
    
    end = perf_counter()
    print("FOR LOOP CLIENT -> Time: ", end - start)


async def for_loop_client_async(number_of_request: int = 50):
    """For loop with async Client session."""
    start = perf_counter()
    
    async with httpx.AsyncClient() as client:
        for i in range(number_of_request):
            res = await client.get(URL)
            print(i, res.json()["author"])
    
    end = perf_counter()
    print("FOR LOOP CLIENT -> Time: ", end - start )


async def tasks_client_async(number_of_request: int = 50):
    """
    Asyncio tasks with AsyncClient.
    A bit more complex to code but WAY more efficient!
    
    Also, this won't process the request in the correct order.
    But it will sort it when finished.
    """
    start = perf_counter()
    tasks = []

    async with httpx.AsyncClient() as client:
        for i in range(number_of_request):
            tasks.append(asyncio.create_task(
                # Can be replace by a custom ASYNC function
                client.get(URL)
            ))
        
        results = await asyncio.gather(*tasks)
        
        print("Number of requests done: ", len(results))
    
    end = perf_counter()
    print("Tasks gather CLIENT -> Time: ", end - start )


if __name__ == "__main__":
    number_of_request = 150
    
    # Sync
    requests_for_loop(number_of_request)
    httpx_for_loop(number_of_request)
    
    # Sync with Client or Session
    requests_for_loop_client_sync(number_of_request)
    httpx_for_loop_client_sync(number_of_request)

    # async
    asyncio.run(for_loop_client_async(number_of_request))
    asyncio.run(tasks_client_async(number_of_request))
