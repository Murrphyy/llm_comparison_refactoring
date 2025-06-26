def main():
    mod = 1000000000.0 + 7
    n, k = list(map(int, input().split()))
    ans = 0
    for i in range(k, n + 2):
        ans += (n + (n - i + 1)) * i // 2 - (0 + (i - 1)) * i // 2 + 1
        ans = int(ans % mod)
    print(ans)
    return

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
