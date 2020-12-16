'''
https://programmers.co.kr/learn/courses/30/lessons/42577
'''

def solution(phone_book):
    p_len = len(phone_book)
    phone_book.sort()
    for i in range(p_len):
        i_len = len(phone_book[i])

        for j in range(i + 1, p_len):
            answer = False

            for k in range(i_len):
                if phone_book[i][k] != phone_book[j][k]:
                    answer = True
                    break

            if answer == False:
                return answer
            
    return True
