# 문자열 my_string이 매개변수로 주어집니다.
# my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# #내장 함수 이용
# def solution(my_string):
#     answer = 0
    
#     for char in my_string:
#         if char.isdigit():
#             answer += int(char)

#     return answer


# # for 문 이용
# def solution(my_string):
#     answer = 0
    
#     for char in my_string:
#         try:
#             answer += int(char)
#         except:
#             continue

#     return answer


# 아스키 코드를 이용해 반복처리
def solution(my_string):
    answer = 0

    for char in my_string:
        # if ord('0') <= ord(char) <= ord('9'):
        if not (ord('A') <= ord(char) <= ord('z')):
            answer += int(char)

    return answer

print(solution('aAb1B2cC34oOp'))