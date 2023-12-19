
# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
# 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
# A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

def solution(A, B):
    answer = 0
    while A != B and answer < 101:

        A = ''.join([A[-1]] + list(A[:-1]))
        answer += 1

    if A != B:
        return -1

    return answer

print(solution("hello", "ohell" )) #1
print(solution("apple", "elppa" )) #-1
print(solution("atat", "tata" )) #1
print(solution("abc", "abc" )) #0
print(solution("abc", "bca" )) #2

# 네 뭐라고요?

# solution=lambda a,b:(b*2).find(a)

# deque 사용법

# from collections import deque
# def solution(A, B):
#     a, b = deque(A), deque(B)
#     for cnt in range(0, len(A)):
#         if a == b:
#             return cnt
#         a.rotate(1)
#     return -1