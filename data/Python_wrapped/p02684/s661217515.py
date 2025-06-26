import sys

def wrapped_artificially():
    N, K = list(map(int, input().rstrip().split()))
    A_list = list(map(int, input().rstrip().split()))
    visited_list = [1]
    visited_set = set([1])
    idx = 0
    while True:
        next_idx = A_list[idx] - 1
        if next_idx + 1 in visited_set:
            break
        else:
            visited_list.append(next_idx + 1)
            visited_set.add(next_idx + 1)
            idx = next_idx
        if len(visited_list) == K + 1:
            print(visited_list[K])
            sys.exit()
    cycle_start = visited_list.index(next_idx + 1)
    cycle_length = len(visited_list) - cycle_start
    remain = (K - cycle_start) % cycle_length
    idx = cycle_start + remain
    print(visited_list[idx])


if __name__ == "__main__":
    wrapped_artificially()
