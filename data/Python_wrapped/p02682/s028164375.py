

def wrapped_artificially():
    score = list(map(int, input().split()))
    answer = 0
    if score[3] - score[0] <= 0:
        answer += score[3]
    else:
        answer += score[0]
        if score[3] - score[0] - score[1] > 0:
            answer -= score[3] - score[0] - score[1]
    print(answer)


if __name__ == "__main__":
    wrapped_artificially()
