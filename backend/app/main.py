from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from .database import SessionLocal, engine, Base
from .models import URL
from .schemas import URLCreate, URLResponse
from .utils import encode_base62

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

BASE_URL = os.getenv("BASE_URL")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/shorten", response_model=URLResponse)
def shorten_url(request: URLCreate, db: Session = Depends(get_db)):
    # Step 1: check if already exists
    existing = db.query(URL).filter(URL.long_url == request.long_url).first()
    if existing:
        return {"short_url": f"{BASE_URL}/{existing.short_code}"}

    # Step 2: create entry without short_code
    url = request.long_url

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    new_url = URL(long_url=url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    # Step 3: generate short_code from ID
    short_code = encode_base62(new_url.id)
    new_url.short_code = short_code

    db.commit()

    return {"short_url": f"{BASE_URL}/{short_code}"}


@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url.long_url)