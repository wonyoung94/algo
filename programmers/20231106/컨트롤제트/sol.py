
# 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 
# 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 
# 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

def solution(s):

    # 스택 원리 그 잡채....
    
    answer = 0
    s_list = []

    for i in s.split():
        if not i.isalpha():
            s_list.append(int(i))
        elif i == "Z":
            s_list.pop()

    answer = sum(s_list)
    return answer

print(solution("1 2 Z 3")) #4
print(solution("10 20 30 40")) #100
print(solution("10 Z 20 Z 1")) #1
print(solution("10 Z 20 Z")) #0
print(solution("-1 -2 -3 Z")) #-3


# 성실하게 하라는대로 Z문자가 나오면 Z문자랑, 그 전 문자 지운 정직한 답변
# def solution(s):
#     myarr = s.split()
#     while 'Z' in myarr:
#         i = myarr.index('Z')
#         del myarr[i]
#         del myarr[i-1]
#     result = 0
#     for s1 in myarr:
#         result += int(s1)
#     return result
