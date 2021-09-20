# 다리를 지나는 트럭
# 2021-09-21

def solution(bridge_length, weight, truck_weights):
    answer, stack = 0, [0] * bridge_length
    while len(stack):
        stack.pop(0)
        if truck_weights:
            if sum(stack) + truck_weights[0] <= weight:
                stack.append(truck_weights.pop(0))
            else:
                stack.append(0)
        else:
            answer += bridge_length
            break
        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))