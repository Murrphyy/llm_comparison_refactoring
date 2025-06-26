def simplify(s):
    res = []
    o = 0
    e = 0
    for c in s:
        if c == ')' and res and (res[-1] == '('):
            res.pop()
            o -= 1
        else:
            res.append(c)
            if c == '(':
                o += 1
            else:
                e += 1
    return (res, o, e)
def submit():
    n = int(input())
    slist = []
    for _ in range(n):
        slist.append(simplify(input()))
    open_only = []
    end_only = []
    mix = []
    for s, o, e in slist:
        if o > 0 and e == 0:
            open_only.append((s, o, e))
        elif o == 0 and e > 0:
            end_only.append((s, o, e))
        else:
            mix.append((s, o, e))
    mix.sort(key=lambda x: x[1] - x[2], reverse=True)
    check = 0
    for s, o, e in open_only:
        check += o
    for s, o, e in mix:
        check -= e
        if check < 0:
            print('No')
            return
        check += o
    for s, o, e in end_only:
        check -= e
    if check == 0:
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    submit()


if __name__ == "__main__":
    wrapped_artificially()
