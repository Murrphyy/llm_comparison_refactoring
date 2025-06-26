from collections import defaultdict
import numpy as np
def main():
    s = input()
    n = len(s)
    d = np.zeros(2019, np.int64)
    ans = 0
    num = 0
    pow10 = 1
    d[0] = 1
    for i in reversed(range(n)):
        pow10 = pow10 * 10 % 2019
        num += int(s[i]) * pow10
        mod = num % 2019
        ans += d[mod]
        d[mod] += 1
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
