'''
https://programmers.co.kr/learn/courses/30/lessons/42576
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = len(participant)
    
    for i in range(n-1):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[n-1]
