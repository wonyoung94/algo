import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+ 1):
    N, M = map(int, input().split())

    result = ''

    #배열 입력 받기
    arr = []
    for i in range(N):
        arr.append(input())

    #  가로 기준점 /  회문의 시작점을 잡기 위한 반복문
    for i in range(N):
        for j in range(N-M+1):
            

            for r in range(M // 2): # 어차피 똑같은거 한번만 확인, 효율성 증대
                    # front : 맨 앞글자부터 한칸씩 증가
                    f = arr[i][j +r]
                    # back : 맨 뒷글자부터 한칸씩 감소
                    b = arr[i][M-1 -r]

                    # 앞과 뒤가 똑같다면
                    if f == b:
                        continue
                    # 앞과 뒤가 다르다면
                    else:
                        break
            # 32번의 break를 만나지 않은 경우 : 끝까지 반복하고 회문을 찾은 경우
            else: 
                for a in range(M):
                    result += arr[i][j +a]


    # 세로 기준점 /  회문의 시작점을 잡기 위한 반복문
    for j in range(N):
        for i in range(N-M+1):


            for c in range(M // 2):
                f = arr[i +c][j]
                b = arr[i+M-1 -c][j]

                if f == b:
                    continue
                else:
                    break
            else:
                for a in range(M):
                    result += arr[i +a][j]

    print(result)
