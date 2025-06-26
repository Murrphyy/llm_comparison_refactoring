

def wrapped_artificially():
    if __name__ == '__main__':
        a, b, c, k = map(int, input().split())
        ans = 0
        if k >= a:
            k -= a
            ans += a
        else:
            ans += k
            print(ans)
            exit()
        if k >= b:
            k -= b
        else:
            print(ans)
            exit()
        if k >= c:
            ans += c * -1
        else:
            ans += k * -1
        print(ans)


if __name__ == "__main__":
    wrapped_artificially()
