from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

from .database import connect_db, get_db
from .schemas import URLCreate, URLResponse
from .utils import encode_base62
from . import queries

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

app = FastAPI()


@app.on_event("startup")
async def startup():
    await connect_db()


@app.post("/api/v1/shorten", response_model=URLResponse)
async def shorten_url(request: URLCreate, conn=Depends(get_db)):

    url = request.long_url

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    # Step 1: Check if URL already exists
    existing = await queries.get_url_by_long_url(conn, url)

    if existing and existing["short_code"]:
        return {"short_url": f"{BASE_URL}/{existing['short_code']}"}

    # Step 2: Insert URL
    row = await queries.insert_url(conn, url)
    id = row["id"]

    # Step 3: Generate short code
    short_code = encode_base62(id)

    # Step 4: Update short code
    await queries.update_short_code(conn, id, short_code)

    return {"short_url": f"{BASE_URL}/{short_code}"}


@app.get("/{short_code}")
async def redirect(short_code: str, conn=Depends(get_db)):

    row = await queries.get_url_by_code(conn, short_code)

    if not row:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(row["long_url"])