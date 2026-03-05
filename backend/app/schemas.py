# Schemas for FastAPI

# These schemas define the structure of the data that will be sent and received by the API endpoints.
# pydantic is used to create these schemas, which provide data validation and serialization.
# examples:
# URLCreate -> schema for creating a new shortened URL, expects a long_url field.
# URLResponse -> schema for the response when a new shortened URL is created, contains the short_url field.

from pydantic import BaseModel

class URLCreate(BaseModel):
    long_url: str

class URLResponse(BaseModel):
    short_url: str