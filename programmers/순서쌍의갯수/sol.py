# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

# for문을 이용해 n 까지 나눠서 나머지가 0인 값의 몫과 묶어준다


# def solution(n):
#     for i in range(1, n+1):
#         if n % i == 0:
#             answer += 1            
#     return answer


def solution(n):
    answer = 0
    for num in range(1, int(n ** 0.5) + 1):
        if n % num == 0:
            answer +=2
            
        if num * num == n:
            answer -= 1
    return answer

print(solution(20))



