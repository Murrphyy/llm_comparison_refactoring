

def wrapped_artificially():
    S = input()
    T = input()
    ans = 'Yes'
    for x, y in zip(S, T):
        if x != y:
            ans = 'No'
            break
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
