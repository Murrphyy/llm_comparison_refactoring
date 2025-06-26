

def wrapped_artificially():
    s, w = [int(i) for i in input().split()]
    ans = 'safe' if s > w else 'unsafe'
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
