'''
https://programmers.co.kr/learn/courses/30/lessons/43162


'''
def dfs(computers, visited, vertex):
    visited[vertex] = 1
    for i in range(len(computers)):
        if computers[vertex][i] and not visited[i]:
            dfs(computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer