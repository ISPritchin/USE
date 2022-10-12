from functools import cache


@cache
def gameResult(x, y):
    if x + y >= 82:
        return 0

    nextCodes = [gameResult(x + 1, y), gameResult(x * 4, y),
                 gameResult(x, y + 1), gameResult(x, y * 4)]

    negative = [c for c in nextCodes if c <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(nextCodes)

    return res
