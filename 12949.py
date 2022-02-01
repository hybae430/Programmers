# 행렬의 곱셈
# 2022-02-01

# def solution(arr1, arr2):
#     answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
#     for i in range(len(arr1)):
#         for j in range(len(arr2[0])):
#             for k in range(len(arr2)):
#                 answer[i][j] += arr1[i][k] * arr2[k][j]
#
#     return answer


# zip 사용 다른 풀이
def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*arr2)] for A_row in arr1]


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
