import sys
import collections
def main():
    n = int(input())
    al = lin()
    aal = [i - v for i, v in enumerate(al)]
    ccl = collections.Counter(aal)
    ret = 0
    for i, v in enumerate(al):
        ccl[i - v] -= 1
        if i + v in ccl:
            ret += ccl[i + v]
    print(ret)
def pa(v):
    if isTest:
        print(v)
def input_clipboard():
    import clipboard
    input_text = clipboard.get()
    input_l = input_text.splitlines()
    for l in input_l:
        yield l

def wrapped_artificially():
    input_methods = ['clipboard', 'file', 'key']
    using_method = 0
    input_method = input_methods[using_method]
    tin = lambda: map(int, input().split())
    lin = lambda: list(tin())
    mod = 1000000007
    isTest = False
    if __name__ == '__main__':
        if sys.platform == 'ios':
            if input_method == input_methods[0]:
                ic = input_clipboard()
                input = lambda: ic.__next__()
            elif input_method == input_methods[1]:
                sys.stdin = open('inputFile.txt')
            else:
                pass
            isTest = True
        else:
            pass
        ret = main()
        if ret is not None:
            print(ret)


if __name__ == "__main__":
    wrapped_artificially()
