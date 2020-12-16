'''
https://programmers.co.kr/learn/courses/30/lessons/42578
'''

from collections import Counter
from itertools import combinations
from functools import reduce

def solution(clothes):
    clothes = [i[1] for i in clothes]
    clothes = list(Counter(clothes).values())
    answer = sum(clothes)

    if len(clothes) == answer:
        return (2 ** answer - 1)

    for i in range(2, len(clothes)+1):
        c = combinations(clothes, i)
        answer = answer + sum(reduce((lambda x, y: x * y), x) for x in c)

    return answer