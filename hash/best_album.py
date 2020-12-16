'''
https://programmers.co.kr/learn/courses/30/lessons/42579
'''

import operator
def solution(genres, plays):
    answer = {}
    temp_sum = {}

    for key in set(genres):
        answer[key] = []
    
    for key in set(genres):
        temp_sum[key] = 0

    temp_cnt = 0
    temp_gp = []

    for i in range(len(genres)):
        temp_gp.append([genres[i],  plays[i], i])

    temp_gp = sorted(temp_gp, key = operator.itemgetter(0, 1), reverse=True)
    prev = ''

    for i in range(len(temp_gp)):
        temp_sum[temp_gp[i][0]] += temp_gp[i][1]
        if prev != temp_gp[i][0]:
            temp_cnt = 1
            answer[temp_gp[i][0]].append(temp_gp[i][:])
            prev = temp_gp[i][0]
        else:
            if temp_cnt == 1:
                answer[temp_gp[i][0]].append(temp_gp[i][:])
                temp_cnt = 0

    temp_sum = sorted(temp_sum.items(), key=lambda kv: kv[1], reverse=True)

    final = []
    for key, value in temp_sum:
        final.append(answer[key][0][2])
        if len(answer[key]) == 2:
            final.append(answer[key][1][2])

    return final