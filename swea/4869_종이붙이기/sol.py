    # N 10 일때 1
    # N 20 일때 3
    # N 30 일떄 5  =  3  + (2*1)
    # N 40 일떄 11 =  5  + (2*3)
    # N 50 일떄 21 =  11 + (2*5)
    # N Ax 일때 Ay = A(x-1) + (2*A(x-2))

    # DP를 사용해서 

def function(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return function(N-10) + 2*function(N-20)

import sys
sys.stdin = open('input.txt')

T = int(input())
answer = 0

for tc in range(1, T+1):
    N = int(input())
    answer = function(N)

    print(f'#{tc} {answer}')

#     import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input()) // 10

#     memo = [0, 1, 3]

#     while N >= len(memo):
#         result = memo[len(memo)-2] * 2 + memo[len(memo)-1]
#         memo.append(result)

#     print(memo[N])