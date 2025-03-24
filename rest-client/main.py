from typing import Union
from fastapi import FastAPI

from lib.util import count_primes
from typing import List
from lib.models import Item


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "I am running"}


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/cpu-intensive")
async def cpu_intensive_task(n: int = 1000000):
    # Simple CPU-intensive task: Count prime numbers up to n
    return {"prime_count": count_primes(n)}


@app.post("/large-payload")
async def large_payload(items: List[Item]):
    # Return a large payload to test response size handling
    return {"received": len(items)}
