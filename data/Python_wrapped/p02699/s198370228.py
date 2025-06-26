

def wrapped_artificially():
    s, w = list(map(int, input().split()))
    a = ''
    if s <= w:
        a = 'un'
    print(a + 'safe')


if __name__ == "__main__":
    wrapped_artificially()
