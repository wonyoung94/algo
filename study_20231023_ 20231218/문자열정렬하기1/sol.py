# 문자열 my_string이 매개변수로 주어질 때,
# my_string 안에 있는 숫자만 골라 
# 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

# isdigit 함수 (내장함수) 사용

def solution(my_string):
    answer = []
    
    for num in my_string:
        if num.isdigit():
            answer.append(int(num))

    return sorted(answer)


print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))

# 변태답안
# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()])


# 람다 썼길래 가져와봄
# def solution(my_string):
#     return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))


# 아스키코드를 이용한 답변
# def solution(my_string):
#     answer = []

#     for i in range(len(my_string)):
#         if ord(my_string[i]) < 65:
#             answer.append(int(my_string[i]))
#         else:
#             continue

#     answer.sort()

#     return answer