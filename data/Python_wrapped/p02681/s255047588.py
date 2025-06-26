

def wrapped_artificially():
    S = input()
    T = input()
    ans = 'No'
    if S != T:
        if S == T[:len(S)]:
            if T[-1].islower():
                ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
