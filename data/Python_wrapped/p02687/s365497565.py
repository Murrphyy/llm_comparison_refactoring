def main():
    print('ARC' if input() == 'ABC' else 'ABC')

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
