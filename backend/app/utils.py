import string

BASE62 = string.digits + string.ascii_letters

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]

    arr = []
    while num:
        num, rem = divmod(num, 62)
        arr.append(BASE62[rem])

    arr.reverse()
    return ''.join(arr)