
# 문자열 my_string이 매개변수로 주어집니다. 
# my_string에서 중복된 문자를 제거하고 
# 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.



def solution(my_string):
    answer = ''

    # answer값에 my_string이 없을 경우에만 append 시킨다
    for char in my_string:
        if char not in answer:
            answer += char
    return answer


print(solution("people")) #"peol"
print(solution("We are the world")) #"We arthwold"




# 내장함수 dict.fromkeys() 사용
# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))

# 한솔이 답변 : 스택 이용
# def solution(my_string):
#     stack = []
#     for char in my_string:
#         # 스택에 아무것도 없다면 추가
#         if len(stack) == 0:
#             stack.append(char)
#         # 스택 안에 문자 있다면 비교
#         else:
#             # 문자가 스택에 없을 때만 추가
#             if char not in stack:
#                 stack.append(char)
            
#     # 문자열로 변환해서 리턴
#     return ''.join(stack)

