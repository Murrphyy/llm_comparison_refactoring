def main():
    a, b, c, k = map(int, input().split())
    if a + b >= k:
        print(min(a, k))
    else:
        print(a - (k - a - b))

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
