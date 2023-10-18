import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 전체 보드의 길이
    # M : 파리채의 길이
    N, M = map(int, input().split())

    # N * N 의 배열을 input 받아오기 위해 이중리스트 생성
    F = [] # Field = 이중리스트를 받기 위한 새로운 필드 생성
    result = 0 # 최종 값

    for i in range(N):
        F.append(list(map(int, input().split())))
    # (r1, c1) 부터 (r1+M-1, c1+M-1) 안에 있는 리스트 데이터 추출
    for i in range(N-M+1):
        for j in range(N-M+1): # 파리채의 기준점을 잡아주는 반복문
            F_part = 0 # 추출될 필드 : 리스트로 해도 구현은 가능하나 sum 함수를 또 해야 하므로 비효율 
            for r in range(M):
                for c in range(M): # 파리채를 그리는 반복문
                    F_part += F[i+r][j+c]

                # 그 안의 값이 가장 큰 값을 추출
                if result < F_part:
                    result = F_part

    print(result)
