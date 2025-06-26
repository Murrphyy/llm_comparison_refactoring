

def wrapped_artificially():
    N, K = map(int, input().split())
    AAA = []
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        AAA = AAA + A
    AAA = list(set(AAA))
    AA = []
    for i in range(N):
        AA = AA + [i + 1]
    a = AAA + AA
    ANS = len([i for i in list(set(a)) if a.count(i) == 1])
    print(ANS)


if __name__ == "__main__":
    wrapped_artificially()
