

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    _sum = 0
    if a > k:
        _sum += k
    else:
        k -= a
        _sum += a
        if b > k:
            b = 0
        else:
            k -= b
            if c > k:
                _sum -= k
            else:
                _sum -= c
    print(_sum)


if __name__ == "__main__":
    wrapped_artificially()
