def main():
    a, b, c, d = map(int, input().split())
    if c % b == 0:
        e = c // b
    else:
        e = c // b + 1
    if a % d == 0:
        f = a // d
    else:
        f = a // d + 1
    if e > f:
        ans = 'No'
    else:
        ans = 'Yes'
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
