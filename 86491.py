# 최소직사각형
# 2021-09-29

def solution(sizes):
    long, short = 1, 1
    for size in sizes:
        if long < max(size):
            long = max(size)
        if short < min(size):
            short = min(size)

        # long = max(long, max(size))
        # short = max(short, min(size))

        # long, short = [], []
        # for size in sizes:
        #     long.append(max(size))
        #     short.append(min(size))

    return long * short

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))