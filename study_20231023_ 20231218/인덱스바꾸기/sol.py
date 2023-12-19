
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을
# return 하도록 solution 함수를 완성해보세요.

def solution(my_string, num1, num2):
    my_list = list(my_string)
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    answer = ''.join(my_list)
    return answer

print(solution("hello", 1, 2)) # "hlelo"
print(solution("I love you", 1, 2)) # "I l veoyou"


# 단순 반복문으로 처리
# def solution(my_string, num1, num2):
#     answer = ""
#     a, b = my_string[num1], my_string[num2]
#     for i in range(len(my_string)):
#         if i == num1:
#             answer += b
#         elif i == num2:
#             answer += a
#         else:
#             answer += my_string[i]
#     return answer