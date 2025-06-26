

def wrapped_artificially():
    N = int(input())
    s = set()
    for _ in range(N):
        S = input()
        if S in s:
            continue
        else:
            s.add(S)
    print(len(s))


if __name__ == "__main__":
    wrapped_artificially()
