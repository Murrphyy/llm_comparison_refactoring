def main():
    k = int(input())
    ab = [int(_x) for _x in input().split()]
    a = ab[0]
    b = ab[1]
    for i in range(a, b + 1):
        if i % k == 0:
            print('OK')
            return
    print('NG')

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
