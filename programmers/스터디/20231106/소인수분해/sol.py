
# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
# 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 
# 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

#이거 해보고 싶어서 함수 깔았음.. 근데 프로그래머스에서 안됨 T.T

# from sympy.ntheory import factorint
# def solution(n):
#     fac = factorint(n)
#     answer = list(fac.keys())
#     return answer

# 내장함수 없이 해보기
# 1~n까지 소수 찾기
# n을 소수로 나눠서, 나누어 떨어지는 소수만 리스트에 append

def solution(n):
    factors = set()  # 중복 제거를 위해 그냥 set

    # 짝수인지 확인(소인수에 2가 들어가는지)
    while n % 2 == 0:
        factors.add(2)
        # 다음 인수 찾기 (420/2=210의 인수 찾기, 2로 안나눠질때까지 while문 못나감)
        n = n // 2

    # 3부터 2step씩 올라가면서 인수 확인하기(짝수를 이미 체크 했으므로)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            # 현재 i가 인수면 set에 넣음
            factors.add(i)
            # 다음 인수 찾기 (105/3=35의 인수 찾기)
            n = n // i  

    # 2보다 큰 다른 소수일 경우 추가(17은 위에 for, while 모두 안걸러질 수 있으므로)
    if n > 2:
        factors.add(n)

    return sorted(list(factors))


print(solution(12)) # [2, 3]
print(solution(17)) # [17]
print(solution(420)) # [2, 3, 5, 7]

# sympy 함수는 파이썬 내장 라이브러리가 아니라 새로 받아줘야함.
# 방정식을 풀 수 있는 라이브러리
# 간단한 소인수분해부터 미.적분까지 활용 가능.


# 정직하게 하나씩 올라가면서 나눠보고 정리함.
# def solution(n):
#     answer = []
#     d = 2
#     while d <= n:
#         if n % d == 0:
#             n /= d
#             if d not in answer:
#                 answer.append(d)
#         else:
#             d += 1
#     return answer