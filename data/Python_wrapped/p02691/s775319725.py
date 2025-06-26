def main():
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    for i in range(n):
        tmp = i - a[i]
        if 0 < tmp:
            J[tmp] += 1
    cnt = 0
    for i in range(n):
        tmp = a[i] + i + 2
        if tmp < len(J) - 1:
            cnt += J[tmp]
    print(cnt)
    return

def wrapped_artificially():
    J = [0 for i in range(int(200000.0 + 3))]
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
