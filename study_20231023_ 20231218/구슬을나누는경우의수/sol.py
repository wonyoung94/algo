
# 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 
# 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.

import math
def solution(balls, share):
    return int(math.factorial(balls)/((math.factorial(balls-share))*(math.factorial(share))))


print(solution(3, 2)) # 3
print(solution(5, 3)) # 10


# combination 함수를 그냥 쓰면 됨...
# import math
# def solution(balls, share):
#     return math.comb(balls, share)

# factorial 구현 + combination 구현
# def solution(balls, share):
#     answer = factorial(balls) / (factorial(balls - share) * factorial(share))
#     return answer

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result

# 민정이 답
# def solution(balls, share):
#     n = 1
#     m = 1
#     nm = 1
#     answer = 0 

#     for i in range(1, balls+1):
#         n *= i 
#     for j in range(1, share+1):
#         m *= j
#     for k in range(1, balls-share +1):
#         nm *= k

#     answer = n / (nm * m)
#     return int(answer)

# print(solution(5,3))
