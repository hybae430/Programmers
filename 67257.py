# 수식 최대화
# 2021-10-06

import re
from itertools import permutations

def solution(expression):
    expression = re.split('([-+*])', expression)
    signs = ['-', '*', '+']
    tmp = list(permutations(signs, 3))

    answer = []
    for t in tmp:
        e = expression[:]
        for sign in t:
            while sign in e:
                idx = e.index(sign)
                e[idx - 1] = str(eval(e[idx - 1] + sign + e[idx + 1]))
                del e[idx:idx + 2]
        answer.append(abs(int(e[0])))

    return max(answer)

# def solution(expression):
#     answer, sign, st, tmp = [], ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*'], [], ''
#
#     for e in expression:
#         if e.isdigit():
#             tmp += e
#         else:
#             st.append(tmp)
#             st.append(e)
#             tmp = ''
#     st.append(tmp)
#
#     for s in sign:
#         tmp2, st2, sign2 = [], st[:], []
#         for i in range(2):
#             if s[i] in st:
#                 while st2:
#                     tmp = st2[0]
#                     if sign2 and sign2[-1] == s[i]:
#                         cal = tmp2.pop() + sign2[-1] + tmp
#                         tmp2.append(str(eval(cal)))
#                         sign2.pop()
#                     else:
#                         if tmp.lstrip("-").isdigit():
#                             tmp2.append(tmp)
#                         else:
#                             sign2.append(tmp)
#                     st2.pop(0)
#                 for x in range(len(sign2)):
#                     st2.append(tmp2[x])
#                     st2.append(sign2[x])
#                 st2.append(tmp2[-1])
#                 tmp2, sign2 = [], []
#             else:
#                 continue
#
#         answer.append(abs(eval(''.join(st2))))
#
#     return max(answer)

print(solution("100-200*300-500+20"))