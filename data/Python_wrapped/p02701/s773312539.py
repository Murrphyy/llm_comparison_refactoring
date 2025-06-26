def l_in(type_):
    return list(map(type_, input().split()))
def i_in():
    return int(input())
def m_in(type_):
    return map(type_, input().split())
def r_in(n, type_):
    return [type_(input()) for _ in range(n)]

def wrapped_artificially():
    ans = None
    n = i_in()
    d = {}
    for _ in range(n):
        k = input()
        d[k] = 1
    ans = len(d)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
