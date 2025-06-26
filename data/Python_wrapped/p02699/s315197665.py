

def wrapped_artificially():
    S, W = map(int, input().split())
    print(('safe', 'unsafe')[W >= S])


if __name__ == "__main__":
    wrapped_artificially()
