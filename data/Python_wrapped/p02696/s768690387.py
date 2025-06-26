def floor(x, A, B):
    return int(A * x / B) - A * int(x / B)
def main():
    A, B, N = map(int, input().split())
    if N <= B - 1:
        res_x = N
    else:
        res_x = B - 1
    res = floor(res_x, A, B)
    print(res)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
