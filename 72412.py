# 순위 검색
# 2022-01-02

def solution(info, query):
    answer, info2, query2, idx = [0 for i in range(len(query))], [], [], 0

    for i in info:
        info2.append(i.split())
    for i in query:
        i = i.replace(" and ", " ")
        query2.append(i.split())

    for q in query2:
        lang, side, car, food, score = q
        for i in info2:
            lang2, side2, car2, food2, score2 = i
            if lang == lang2 or lang == "-":
                if side == side2 or side == "-":
                    if car == car2 or car == "-":
                        if food == food2 or food == "-":
                            if int(score) <= int(score2):
                                answer[idx] += 1
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        idx += 1

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))