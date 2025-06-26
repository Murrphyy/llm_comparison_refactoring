

def wrapped_artificially():
    l = input().split()
    n1 = int(l[0])
    n0 = int(l[1])
    n = int(l[2])
    k = int(l[3])
    ans = 0
    if k >= n1:
        ans += n1
    else:
        ans += k
    k -= n1
    k -= n0
    if k > 0:
        ans -= k
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
