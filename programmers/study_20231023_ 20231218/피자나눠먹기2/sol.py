
# 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
# 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
# n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 
# 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

def solution(n):

    for i in range(1, n+1):
        if i * 6 % n == 0:
            return i


print(solution(6)) #1
print(solution(10)) #5
print(solution(4)) #2




# def solution(n):
#     answer = 1
#     while 6 * answer % n:
#         answer += 1
#     return answer



# math 함수 호출(3.9부터 지원하여 프로그래머스에선 실행 불가)
# I am Instead of the GCD function provided by Python and lcm, the least common multiple function, 
# we used mathematics to find the least common multiple. 
# (The lcm function is not provided due to a lower version.)
# GCD함수(greatest common divisor) : 최대공약수를 찾는 함수, 유클리드알고리즘 관련 
# 유클리드 호제법 관련 문서 : https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95

# import math

# def solution(n):
#     return (n * 6) // math.gcd(n, 6) // 6

