def resolve():
    N = int(input())
    prizes = set()
    for i in range(N):
        prizes.add(input())
    print(len(prizes))

def wrapped_artificially():
    if '__main__' == __name__:
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
