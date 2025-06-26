

def wrapped_artificially():
    X = int(input())
    dep = 100
    count = 0
    while X > dep:
        dep = 101 * dep // 100
        count += 1
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
