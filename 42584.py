# 주식가격

def solution(prices):
    answer = []
    m = 1
    for idx, p in enumerate(prices):
        if p == 1:
            answer.append(len(prices) - idx - 1)
        elif idx == (len(prices) - 1):
            answer.append(0)
        else:
            tmp = idx + 1
            for x in range(tmp, len(prices)):
                if prices[x] < p:
                    answer.append(x - idx)
                    break
            else:
                answer.append(len(prices)- idx -1)
    return answer