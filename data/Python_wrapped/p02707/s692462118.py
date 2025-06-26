

def wrapped_artificially():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    adj = [0] * 10 ** 6
    count = 0
    for i in a:
        adj[i] += 1
    for i in range(n):
        print(adj[i + 1])


if __name__ == "__main__":
    wrapped_artificially()
