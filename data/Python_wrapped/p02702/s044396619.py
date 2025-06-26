

def wrapped_artificially():
    S = input()
    P = 2019
    ans = 0
    count = [0] * P
    count[0] = 1
    u = 0
    for i, s in enumerate(reversed(S)):
        u = (int(s) * pow(10, i, P) + u) % P
        ans += count[u]
        count[u] += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
