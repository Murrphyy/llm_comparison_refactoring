class tower:

    def __init__(self, H):
        self.H = H
        self.neighbors = []
        self.checked = False

    def add_path(self, a):
        self.neighbors.append(a)

def wrapped_artificially():
    N, M = [int(i) for i in input().split()]
    Hs = [int(i) for i in input().split()]
    T = {}
    for i in range(N):
        T[i + 1] = tower(Hs[i])
    for i in range(M):
        A, B = [int(i) for i in input().split()]
        T[A].add_path(B)
        T[B].add_path(A)
    items_sorted = sorted(T.items(), key=lambda x: x[1].H, reverse=1)
    counter = 0
    for each in items_sorted:
        i = each[0]
        t = each[1]
        if t.checked:
            continue
        else:
            t.checked = True
            flag = True
            for a in t.neighbors:
                T[a].checked = True
                if t.H <= T[a].H:
                    flag = False
            if flag:
                counter += 1
    print(counter)


if __name__ == "__main__":
    wrapped_artificially()
