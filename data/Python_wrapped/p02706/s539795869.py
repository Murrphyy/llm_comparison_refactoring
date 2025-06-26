

def wrapped_artificially():
    x = input()
    x_list = x.split()
    N = int(x_list[0])
    M = int(x_list[1])
    y = input()
    y_list = y.split()
    sum1 = 0
    count = 0
    for i in range(M):
        s = int(y_list[count])
        count += 1
        sum1 += s
    if N >= sum1:
        print(N - sum1)
    else:
        print(-1)


if __name__ == "__main__":
    wrapped_artificially()
