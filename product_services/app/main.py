
from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import AsyncGenerator
from aiokafka import AIOKafkaConsumer
import asyncio


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "product_services" }
    