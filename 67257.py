# 수식 최대화
# 2021-10-02

import re

def solution(expression):
    answer, sign, st = [1], ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*'], []
    con = re.split('\* | - | + ', expression)
    print(con)
    # for exp in expression:

    return max(answer)

print(solution("100-200*300-500+20"))