import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A = list(range(1,13))
    N, K = list(map(int, input().split()))

# A 의 부분집합을 구한다
# N, K의 조건에 맞는 부분집합을 찾는다
# 해당하는 부분집합이 없는경우 0을 출력한다. - 처음 count 값이 0이므로 따로 구현할 필요 없음
# 조건이 맞는 부분집합이 있는 경우 갯수를 카운팅한다.

    count = 0

    for i in range(1<<len(A)):
        temp = []
        for j in range(len(A)):
            if i & (1 << j):
                temp.append(A[j])

        # print(temp) : 모든 부분집합 출력

        if len(temp) == N and sum(temp) == K:
            count += 1

        # 조건에 맞는 부분집합 갯수 카운팅

    print(f'#{tc} {count}')