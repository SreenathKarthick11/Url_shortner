async def get_url_by_long_url(conn, long_url: str):
    query = """
    SELECT id, long_url, short_code
    FROM urls
    WHERE long_url = $1
    LIMIT 1
    """
    return await conn.fetchrow(query, long_url)


async def insert_url(conn, long_url: str):
    query = """
    INSERT INTO urls (long_url)
    VALUES ($1)
    RETURNING id
    """
    return await conn.fetchrow(query, long_url)


async def update_short_code(conn, id: int, short_code: str):
    query = """
    UPDATE urls
    SET short_code = $1
    WHERE id = $2
    """
    await conn.execute(query, short_code, id)


async def get_url_by_code(conn, short_code: str):
    query = """
    SELECT long_url
    FROM urls
    WHERE short_code = $1
    LIMIT 1
    """
    return await conn.fetchrow(query, short_code)