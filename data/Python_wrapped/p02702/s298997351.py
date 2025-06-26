from collections import Counter
def choose2(x):
    return x * (x - 1) // 2

def wrapped_artificially():
    s = input()
    r = [0]
    for d in map(int, s):
        r.append((r[-1] * 10 + d) % 2019)
    e = 1
    for i in range(len(r) - 1, -1, -1):
        r[i] = r[i] * e % 2019
        e = e * 10 % 2019
    counter = Counter(r)
    print(sum((choose2(counter[i]) for i in counter)))


if __name__ == "__main__":
    wrapped_artificially()
