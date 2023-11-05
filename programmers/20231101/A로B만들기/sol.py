
# 문자열 before와 after가 매개변수로 주어질 때,
# before의 순서를 바꾸어 after를 만들 수 있으면 1을, 
# 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.


def solution(before, after):
    
    answer = 0

    if sorted(before) == sorted(after):
        answer +=1
    return answer

#정렬해서 같으면 1, 다르면 0 하면 되는거 아닌가



print(solution("olleh","hello")) # 1
print(solution("allpe","apple")) # 0

# 딱히 맘에드는건 없고, 그냥 깔끔해보이는거 하나만 들고옴 
# def solution(before, after):
#     return 1 if sorted(before)==sorted(after) else 0

# 민정이 답
# def solution(before, after):
#     sort_bef = sorted(before)
#     sort_aft = sorted(after)
#     if sort_bef == sort_aft:
#         return 1
#     else:
#         return 0
# print(solution("olleh","hello"))

# 한솔이 답
# def solution(before, after):
#     # before에 있는 문자열이 after에 있다면 
#     for char in before:
#         if char in after:
#             # replace 이용해서 1개만 '0'으로 바꾸기
#             before = before.replace(char, '0', 1)
#             after = after.replace(char, '0', 1)

#     # 반복문 종료 후 before와 after가 서로 같다면 문자열 내부 문자 갯수가 동일하단 의미
#     if before == after:
#         return 1
#     else:
#         return 0