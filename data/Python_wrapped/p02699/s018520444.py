def main(s, w):
    if s > w:
        return 'safe'
    else:
        return 'unsafe'

def wrapped_artificially():
    if __name__ == '__main__':
        S, W = map(int, input().split(' '))
        print(main(S, W))


if __name__ == "__main__":
    wrapped_artificially()
