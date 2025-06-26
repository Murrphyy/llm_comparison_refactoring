def solve():
    S = input()
    T = input()
    expected_T = S + T[-1]
    if expected_T == T:
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
