

def wrapped_artificially():
    K = int(input().rstrip())
    distance_range = list(map(int, input().split()))
    if distance_range[1] // K * K >= distance_range[0]:
        print('OK')
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
