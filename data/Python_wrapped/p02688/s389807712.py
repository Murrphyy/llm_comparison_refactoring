import itertools

def wrapped_artificially():
    n, k = map(int, input().split())
    di = [0] * k
    Ai_di = []
    for i in range(k):
        di[i] = int(input())
        Ai_di.append(list(map(int, input().split())))
    ans_set = set(list(itertools.chain.from_iterable(Ai_di)))
    print(n - len(ans_set))


if __name__ == "__main__":
    wrapped_artificially()
