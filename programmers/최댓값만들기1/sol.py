# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# for 문을 통한 방법 (이해는 안감)
# def solution(numbers):
#     answer = 0

#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             multi = numbers[i] * numbers[j]

#             if answer < multi:
#                 answer = multi

#     return answer

# 내가 한 방법
# def solution(numbers):
#     s_numbers = sorted(numbers, reverse=True)
#     num1 = s_numbers[0]
#     num2 = s_numbers[1]
    
#     answer = num1 * num2
#     return answer

def solution(numbers):
    answer = 0

    numbers.sort()

    answer = numbers[-1] * numbers[-2]

    return answer



print(solution([1, 2, 3, 4, 5]))