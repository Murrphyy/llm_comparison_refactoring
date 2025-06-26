

def wrapped_artificially():
    x = int(input())
    r = 100
    ans = 0
    while r < x:
        r = int(r * 101) // 100
        ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
