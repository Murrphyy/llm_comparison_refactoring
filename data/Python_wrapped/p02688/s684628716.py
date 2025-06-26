from itertools import chain
def solve(N, A):
    sunukes = [1 for _ in range(N)]
    for a in A:
        for i in a:
            sunukes[i - 1] = 0
    return sum(sunukes)
def main():
    N, K = map(int, input().split())
    A = []
    for k in range(K):
        _ = int(input())
        A.append(list(map(int, input().split())))
    answer = solve(N, A)
    print(answer)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
