# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.\
# 0 < n ≤ 1000

# 내가 쓴 답
# def solution(n):
#     answer = 0

#     result = 0
#     for answer in range(1,n+1):
#         if answer % 2 == 0:
#             result = answer + result #이쪽 문제같음 확인 필요
#         else:
#             pass
#     return result

# 강사님 답 1
# def solution(n):
#     answer = 0

#     numbers = range(1, n+1)
#     for number in numbers:
#         if number % 2 == 0:
#             answer = answer + number
#         else:
#             pass
#     return result
# print(solution(10))

# 강사님 답 2
def solution(n):
    numbers = range(2, n+1, 2)
    return sum(numbers)

print(solution(10))
print(solution(4))
