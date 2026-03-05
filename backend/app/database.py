# database.py - SQLAlchemy setup for URL shortening service

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# create_engine -> connect to the database with the provided URL
engine = create_engine(DATABASE_URL)

# sessionmaker -> create a new session for interacting with the database
# autocommit=False -> changes are not automatically committed to the database
# autoflush=False -> changes are not automatically flushed to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base -> base class for our ORM models
Base = declarative_base()