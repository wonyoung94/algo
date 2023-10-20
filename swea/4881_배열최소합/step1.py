import sys
sys.stdin = open('input.txt')

T = int(input())
# T = 1

def search(idx):
    if idx >= N:
        print(result)
        return

    # 모든 경우의 수를 탐색
    for i in range(N):
        # print(idx, i, '=', numbers[idx][i])
        result.append(numbers[idx][i])
        search(idx+1)
        result.pop()

for tc in range(1, T+1):
    N = int(input())

    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)

    result = []

    search(0)

    