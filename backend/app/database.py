# database.py - Database connection management for URL shortening service
# This module sets up the connection pool to the PostgreSQL database using asyncpg.
# It provides a function to connect to the database and a dependency function
# to acquire a connection for use in API endpoints.

import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

pool = None

# connect_db -> 
# initializes the connection pool to the PostgreSQL database using the provided DATABASE_URL.
async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

# get_db -> 
# a dependency function that acquires a connection from the pool for use in API endpoints.
async def get_db():
    async with pool.acquire() as connection:
        yield connection