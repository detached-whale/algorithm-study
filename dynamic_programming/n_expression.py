'''
https://programmers.co.kr/learn/courses/30/lessons/42895
'''

def solution(N, number):
    if N == 1 or N == number:
        return N % number + 1

    p = [[] for i in range(9)]
    p[1] = {N}
    p[2] = {int(str(N)*2), N+N, N-N, N*N, N//N}

    if number in p[2]:
        return 2

    for i in range(3, 9):
        temp = {int(str(N)*i)}
        for x in (1, i//2 + 1):
            for y in p[x]:
                for z in p[i - x]:
                    temp.add(y + z)
                    temp.add(y - z)
                    temp.add(z - y)
                    temp.add(y * z)
                    if z != 0:
                        temp.add(y//z)
                    if y != 0:
                        temp.add(z//y)

                    if number in temp:
                        return i
        p[i] = temp

    return -1