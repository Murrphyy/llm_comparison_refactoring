

def wrapped_artificially():
    ans = set()
    n = int(input())
    for i in range(n):
        ans.add(str(input()))
    print(len(ans))


if __name__ == "__main__":
    wrapped_artificially()
