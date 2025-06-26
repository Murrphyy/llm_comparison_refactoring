import sys, math, collections, itertools

def wrapped_artificially():
    input = sys.stdin.readline
    S = input().rstrip()
    Smod2019 = [0]
    num = 0
    deg = 0
    for i in range(len(S) - 1, -1, -1):
        num = (num + int(S[i]) * pow(10, deg, 2019)) % 2019
        Smod2019.append(num)
        deg += 1
    Sc = collections.Counter(Smod2019)
    cnt = 0
    for val in Sc.values():
        cnt += val * (val - 1) // 2
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
