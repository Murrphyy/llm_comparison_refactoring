

def wrapped_artificially():
    n = int(input())
    l = 0
    r = 0
    cntl = 0
    cntr = 0
    fl = 0
    fr = 0
    exl = 0
    exr = 0
    only_r = 0
    only_l = 0
    maxl = 0
    maxr = 0
    exlr = []
    for i in range(n):
        s = input()
        templ = 0
        tempr = 0
        temp_exl = 0
        temp_exr = 0
        fl = 0
        fr = 0
        for i in s:
            if i == '(':
                tempr += 1
            elif i == ')':
                tempr -= 1
                if tempr < 0:
                    tempr = 0
                    templ += 1
                    fl = 1
        temp_exl += templ
        if tempr > 0:
            temp_exr += tempr
            fr = 1
        if fl == 1 and fr == 0:
            only_l += temp_exl
        elif fr == 1 and fl == 0:
            only_r += temp_exr
        elif temp_exl + temp_exr > 0:
            exl += temp_exl
            exr += temp_exr
            exlr.append([temp_exl - temp_exr, temp_exl, temp_exr])
    a = only_r
    b = only_l
    exlr.sort(key=lambda x: x[1])
    exlr.sort()
    for i in range(len(exlr)):
        if exlr[i][1] <= a and exlr[i][0] <= 0:
            a -= exlr[i][0]
            exlr[i] = [0, 0, 0]
    for i in exlr:
        a -= i[1]
        if a < 0:
            print('No')
            exit()
        a += i[2]
    if a - b == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
