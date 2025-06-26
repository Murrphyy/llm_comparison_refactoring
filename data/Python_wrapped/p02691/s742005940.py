from collections import Counter

def wrapped_artificially():
    n = int(input())
    y = list(map(int, input().split()))
    lhs = Counter([j + y[j] for j in range(n)])
    rhs = Counter([j - y[j] for j in range(n)])
    count = 0
    for i in lhs:
        if i in rhs:
            count += lhs[i] * rhs[i]
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
