from collections import Counter

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    i_l = []
    j_l = []
    for i in range(n):
        i_l.append(i + a[i])
        j_l.append(i - a[i])
    ci = Counter(i_l)
    cl = Counter(j_l)
    ans = 0
    for k, v in ci.items():
        ans += v * cl[k]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
