

def wrapped_artificially():
    s, w = (int(i) for i in input().split())
    print('safe') if s > w else print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
