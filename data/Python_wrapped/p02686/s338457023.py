

def wrapped_artificially():
    dicpos = {}
    dicneg = {}
    N = int(input())
    for i in range(N):
        buf = [0]
        for s in input():
            if s == '(':
                buf.append(buf[-1] + 1)
            else:
                buf.append(buf[-1] - 1)
        low = min(buf)
        last = buf[-1]
        if last > 0:
            if low in dicpos:
                dicpos[low].append(last)
            else:
                dicpos[low] = [last]
        elif low - last in dicneg:
            dicneg[low - last].append(-last)
        else:
            dicneg[low - last] = [-last]
    neg_sorted = sorted(dicneg.items(), key=lambda x: x[0], reverse=True)
    pos_sorted = sorted(dicpos.items(), key=lambda x: x[0], reverse=True)
    summ = 0
    flag = 0
    for i in pos_sorted:
        if flag == 1:
            break
        for j in i[1]:
            if summ + i[0] < 0:
                flag = 1
                print('No')
                break
            summ += j
    summ2 = 0
    if flag == 0:
        for i in neg_sorted:
            if flag == 1:
                break
            for j in i[1]:
                if summ2 + i[0] < 0:
                    flag = 1
                    print('No')
                    break
                summ2 += j
    if flag == 0:
        if summ == summ2:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    wrapped_artificially()
