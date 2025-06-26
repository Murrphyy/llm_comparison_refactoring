

def wrapped_artificially():
    s = input()
    s = s[::-1]
    n = len(s)
    rem2019_cnts = [0] * 2019
    rem2019_cnts[0] = 1
    curr_rem = int(s[0])
    rem2019_cnts[curr_rem] = 1
    curr_10_rem = 1
    ans = 0
    for i, si in enumerate(s[1:]):
        sint = int(si)
        next_10_rem = curr_10_rem * 10 % 2019
        next_rem = (next_10_rem * sint + curr_rem) % 2019
        ans += rem2019_cnts[next_rem]
        rem2019_cnts[next_rem] += 1
        curr_10_rem = next_10_rem
        curr_rem = next_rem
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
