

def wrapped_artificially():
    N, K = map(int, input().split())
    A = [int(x) - 1 for x in input().split()]
    seen = {0}
    town = 0
    while K > 0:
        town = A[town]
        K -= 1
        if town in seen:
            break
        seen.add(town)
    start = town
    i = 0
    while K > 0:
        town = A[town]
        i += 1
        K -= 1
        if town is start:
            break
    K = K % i if i > 0 else 0
    while K > 0:
        town = A[town]
        i += 1
        K -= 1
    print(town + 1)


if __name__ == "__main__":
    wrapped_artificially()
