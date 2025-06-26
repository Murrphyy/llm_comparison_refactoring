def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = {}
    answer = 0
    for i in range(n):
        b.append(a[i] + i + 1)
        tmp = -a[i] + i + 1
        if tmp in c:
            c[tmp] += 1
        else:
            c[tmp] = 1
    for i in range(n):
        if b[i] in c:
            answer += c[b[i]]
    print(answer)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
