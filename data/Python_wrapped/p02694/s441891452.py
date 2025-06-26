def main():
    n = int(input())
    print(b(n))
def b(n: int) -> int:
    m = 100
    i = 0
    while True:
        m = m * 101 // 100
        i += 1
        if m >= n:
            break
    return i

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
