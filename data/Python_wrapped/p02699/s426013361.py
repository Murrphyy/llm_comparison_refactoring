

def wrapped_artificially():
    a, b = list(map(int, input().split()))
    if a <= b:
        my_result = 'unsafe'
    else:
        my_result = 'safe'
    print(my_result)


if __name__ == "__main__":
    wrapped_artificially()
