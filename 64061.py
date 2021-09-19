# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        d = i - 1
        for j in board:
            if j[d]:
                if basket:
                    if basket[-1] == j[d]:
                        answer += 2
                        basket.pop()
                        j[d] = 0
                        break
                basket.append(j[d])
                j[d] = 0
                break
    return answer