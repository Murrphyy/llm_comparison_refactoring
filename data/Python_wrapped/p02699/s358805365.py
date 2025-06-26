

def wrapped_artificially():
    S, W = (int(x) for x in input().split())
    if S > W:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
