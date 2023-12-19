
# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
# 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
# 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

import math

def solution(n):
    i = 1
    while math.factorial(i) <= n:
        i +=1
    return i-1

    # while문을 돌려서 result ! 값이 n값보다 클때 멈춘다.


print(solution(3628800)) #10
print(solution(7)) #3

# 나눗셈으로 접근, 1로나누고, 2로나누고, 3으로 나누고....n으로 나눠서 1이되면 그 값을 출력
# 민정이가 이렇게 했음!!!
# def solution(n):
#     divider=0
#     while 1:
#         divider+=1
#         if n/divider < 1:
#             break
#         else:
#             n/=divider
#     return divider-1