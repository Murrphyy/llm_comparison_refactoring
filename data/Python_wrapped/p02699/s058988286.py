

def wrapped_artificially():
    input_line = input().split(' ')
    S = int(input_line[0])
    W = int(input_line[1])
    if S > W:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
