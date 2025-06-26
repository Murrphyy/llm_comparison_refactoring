from collections import Counter
def main():
    n = int(input())
    a = list(map(int, input().split()))
    bigger = [None] * n
    smaller = [None] * n
    for i, ai in enumerate(a):
        bigger[i] = i - ai
        smaller[i] = i + ai
    b = sorted(Counter(bigger).items())
    s = sorted(Counter(smaller).items())
    nb = len(b)
    ns = len(s)
    b.append((10 ** 10, 0))
    s.append((10 ** 11, 0))
    i, j = (0, 0)
    ans = 0
    while i < nb or j < ns:
        bi, nbi = b[i]
        si, nsi = s[j]
        if bi == si:
            ans += nbi * nsi
            i += 1
            j += 1
        elif bi > si:
            j += 1
        else:
            i += 1
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
