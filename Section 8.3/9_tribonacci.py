def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def loop(n):
        result = cache.get(n)
        if result is None:
            result = loop(n - 3) + loop(n - 2) + loop(n - 1)
            cache[n] = result
        return result

    return loop(n)


print(tribonacci(300))
