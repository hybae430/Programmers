# 영어 끝말잇기
# 2022-05-05

def solution(n, words):
    answer = [0, 0]
    sn, last, wordlist = 1, '', []
    for i in range(0, len(words), n):
        wordset = words[(sn - 1)*n:(sn)*n]
        for word in wordset:
            if word not in wordlist and len(word) > 1:
                if not last or last == word[0]:
                    last = word[-1]
                elif last and last != word[0]:
                    return [wordset.index(word) + 1, sn]
                wordlist.append(word)
            else:
                return [wordset.index(word) + 1, sn]
        sn += 1

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))