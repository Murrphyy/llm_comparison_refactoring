def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    setS = set()
    for i in S:
        setS.add(i)
    ans = len(setS)
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
