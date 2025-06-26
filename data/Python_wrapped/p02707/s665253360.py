

def wrapped_artificially():
    n = int(input())
    boss = [int(i) - 1 for i in input().split()]
    sub = {i: 0 for i in range(n)}
    for b in boss:
        sub[b] += 1
    for m in range(n):
        print(sub[m])


if __name__ == "__main__":
    wrapped_artificially()
