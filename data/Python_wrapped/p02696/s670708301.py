def main():
    A, B, N = map(int, input().split())
    x = min(B - 1, N)
    ans = A * x // B - A * (x // B)
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
