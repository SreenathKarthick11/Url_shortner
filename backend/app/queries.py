# queries.py - Database query functions for URL shortening service
# These functions interact with the database to perform CRUD operations
# related to URL shortening.
# Each function takes a database connection and relevant parameters,
#  executes a SQL query, and returns the result.

# get_url_by_long_url -> 
# checks if a long URL already exists in the database and returns its details.
async def get_url_by_long_url(conn, long_url: str):
    query = """
    SELECT id, long_url, short_code
    FROM urls
    WHERE long_url = $1
    LIMIT 1
    """
    return await conn.fetchrow(query, long_url)

# insert_url -> 
# inserts a new long URL into the database and returns the generated ID.
async def insert_url(conn, long_url: str):
    query = """
    INSERT INTO urls (long_url)
    VALUES ($1)
    RETURNING id
    """
    return await conn.fetchrow(query, long_url)

# update_short_code -> 
# updates the short code for a given URL ID after it has been generated.
async def update_short_code(conn, id: int, short_code: str):
    query = """
    UPDATE urls
    SET short_code = $1
    WHERE id = $2
    """
    await conn.execute(query, short_code, id)

# get_url_by_code -> 
# retrieves the long URL associated with a given short code for redirection purposes.
async def get_url_by_code(conn, short_code: str):
    query = """
    SELECT long_url
    FROM urls
    WHERE short_code = $1
    LIMIT 1
    """
    return await conn.fetchrow(query, short_code)