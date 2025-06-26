def pdebut(s):
    o = 0
    for c in s:
        if c == '(':
            o += 1
        else:
            o -= 1
        if o < 0:
            return False
    return o >= 0
def pfin(s):
    c = 0
    for o in s[::-1]:
        if o == ')':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c >= 0
def valuer(s):
    o = 0
    for c in s:
        if c == '(':
            o += 1
        else:
            o -= 1
    return o
def cle(x):
    return -x[1]
def Bon(s):
    o = 0
    for c in s:
        if c == '(':
            o += 1
        else:
            o -= 1
        if o < 0:
            return False
    return o == 0

def wrapped_artificially():
    n = int(input())
    val = [0] * (n + 1)
    tab = []
    debut = []
    fin = []
    milieu = []
    for i in range(n):
        s = input()
        tab.append(s)
        if pdebut(s):
            debut += [i]
        elif pfin(s):
            fin += [i]
        else:
            val[i] = valuer(s)
            milieu += [i]
    couples = [[i, val[i]] for i in milieu]
    couples.sort(key=cle)
    S = ''.join((tab[i] for i in debut))
    S += ''.join((tab[c[0]] for c in couples))
    S += ''.join((tab[i] for i in fin))
    print('Yes' if Bon(S) else 'No')


if __name__ == "__main__":
    wrapped_artificially()
