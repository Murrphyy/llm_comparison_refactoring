import io
import sys
import math
def solve():
    pass
def main():
    n, *a = open(0).read().split()
    s_list = list(a)
    ans = str(len(set(s_list)))
    print(ans)
    return ans
def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB:
        print(f'[deb] {str}')

def wrapped_artificially():
    _DEB = 0
    _INPUT = '5\ngrape\ngrape\ngrape\ngrape\ngrape\n'
    _EXPECTED = '1\n'
    if __name__ == '__main__':
        if _DEB:
            sys.stdin = io.StringIO(_INPUT)
            print('!! Debug Mode !!')
        ans = main()
        if _DEB:
            print()
            if _EXPECTED.strip() == ans.strip():
                print('!! Success !!')
            else:
                print(f'!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}')


if __name__ == "__main__":
    wrapped_artificially()
