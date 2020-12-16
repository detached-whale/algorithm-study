'''
https://programmers.co.kr/learn/courses/30/lessons/43105
'''

def solution(triangle):
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]

    for i in range(2, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][len(triangle[i])-1] += triangle[i-1][len(triangle[i-1])-1]

        for j in range(1, len(triangle[i]) - 1):
            if triangle[i - 1][j - 1] > triangle[i-1][j]:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += triangle[i - 1][j]

    return max(triangle[len(triangle)-1])