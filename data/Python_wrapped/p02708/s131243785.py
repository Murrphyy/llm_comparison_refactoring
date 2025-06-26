

def wrapped_artificially():
    n, k = map(int, input().split())
    count = 0
    for i in range(k, n + 2):
        if i == k:
            tot_min = 0
            tot_max = 0
            for j in range(i):
                tot_min += j
                tot_max += n - j
        else:
            tot_min += i - 1
            tot_max += n - i + 1
        count += tot_max - tot_min + 1
    count %= 10 ** 9 + 7
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
