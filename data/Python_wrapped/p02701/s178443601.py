def readinput():
    n = int(input())
    sList = []
    for _ in range(n):
        sList.append(input())
    return (n, sList)
def main(n, sList):
    keihin = {}
    for s in sList:
        if s in keihin:
            keihin[s] += 1
        else:
            keihin[s] = 1
    return len(keihin)

def wrapped_artificially():
    if __name__ == '__main__':
        n, sList = readinput()
        ans = main(n, sList)
        print(ans)


if __name__ == "__main__":
    wrapped_artificially()
