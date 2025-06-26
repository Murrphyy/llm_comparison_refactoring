

def wrapped_artificially():
    num_of_sheep, num_of_wolf = map(int, input().split())
    if num_of_sheep > num_of_wolf:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
