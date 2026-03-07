from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from .database import connect_db, get_db
from .schemas import URLCreate, URLResponse
from .utils import encode_base62
from . import queries

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_db()
    print("Database connected")

    yield

    # Shutdown (optional cleanup)
    print("Application shutting down")


app = FastAPI(lifespan=lifespan)


@app.post("/api/v1/shorten", response_model=URLResponse)
async def shorten_url(request: URLCreate, conn=Depends(get_db)):

    url = request.long_url

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    # Check existing
    existing = await queries.get_url_by_long_url(conn, url)

    if existing and existing["short_code"]:
        return {"short_url": f"{BASE_URL}/{existing['short_code']}"}

    # Insert URL
    row = await queries.insert_url(conn, url)
    id = row["id"]

    # Generate short code
    short_code = encode_base62(id)

    # Update row
    await queries.update_short_code(conn, id, short_code)

    return {"short_url": f"{BASE_URL}/{short_code}"}


@app.get("/{short_code}")
async def redirect(short_code: str, conn=Depends(get_db)):

    row = await queries.get_url_by_code(conn, short_code)

    if not row:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(row["long_url"])