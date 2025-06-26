

def wrapped_artificially():
    S = input()
    T = 'R' if S[1] == 'B' else 'B'
    print(S[0] + T + S[2])


if __name__ == "__main__":
    wrapped_artificially()
