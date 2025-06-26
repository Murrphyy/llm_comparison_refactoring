import sys
def main():
    a, b, c, k = list(map(int, input().split()))
    if k > a:
        ans = a * 1
        k -= a
    else:
        ans = k * 1
        k = 0
    if k > b:
        k -= b
    else:
        k = 0
    if k > c and k > 0:
        ans += c * -1
    else:
        ans += k * -1
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
