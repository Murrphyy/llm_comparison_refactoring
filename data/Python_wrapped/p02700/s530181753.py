

def wrapped_artificially():
    tkhp, tkat, aohp, aoat = map(int, input().split())
    while True:
        aohp -= tkat
        if aohp <= 0:
            print('Yes')
            exit()
        tkhp -= aoat
        if tkhp <= 0:
            print('No')
            exit()


if __name__ == "__main__":
    wrapped_artificially()
