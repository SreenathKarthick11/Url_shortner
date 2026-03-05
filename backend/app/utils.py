# Utility functions for URL shortening

import string

BASE62 = string.digits + string.ascii_letters

# encode_base62 -> converts an integer to a base62 string, 
# which is used for generating short codes for URLs.
def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]

    arr = []
    while num:
        num, rem = divmod(num, 62)
        arr.append(BASE62[rem])

    arr.reverse()
    return ''.join(arr)