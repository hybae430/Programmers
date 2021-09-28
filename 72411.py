# 메뉴 리뉴얼
# 2021-09-29

from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        nums = {}
        for order in orders:
            order = sorted(order)
            tmp = list(combinations(order, i))
            for t in tmp:
                k = nums.get(t, 0)
                nums[t] = k + 1
        for key, value in nums.items():
            if value == max(nums.values()) and max(nums.values()) > 1:
                answer.append(''.join(key))
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))