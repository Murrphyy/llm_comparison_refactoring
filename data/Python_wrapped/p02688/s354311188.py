

def wrapped_artificially():
    N, K = map(int, input().split())
    vec = [0] * N
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for i in range(d):
            vec[A[i] - 1] += 1
    print(vec.count(0))


if __name__ == "__main__":
    wrapped_artificially()
