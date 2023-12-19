
# 머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 
# 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
# 정수 M, N이 매개변수로 주어질 때, 
# M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.

#이게 왜 됨?
def solution(M, N):
    return (M * N) - 1


print(solution(2, 2)) #3
print(solution(2, 5)) #9
print(solution(1, 1)) #0

# 이게 정석에 더 가까움
# def solution(M, N):
#     answer = 0
#     M,N = max(M,N), min(M,N)
#     answer = (M-1) + (N-1)*M
#     return answer