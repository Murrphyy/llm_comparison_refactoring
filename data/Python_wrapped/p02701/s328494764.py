import sys
import itertools
def resolve(in_):
    return len(set((s.strip() for s in itertools.islice(in_, 1, None))))
def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
