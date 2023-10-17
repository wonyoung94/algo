import sys
sys.stdin = open('input.txt')

# 파란색 시작점에서 빨간색 끝점
# A ~ B, C ~ D 라고 하면 B ~ C 까지의 구간 : 겹치는 구간
# 파란색도 빨간색도 해당하면 두 값을 더했을때 3이 나온다

T = int(input()) 

for tc in range(1, T+1):
    N = int(input())
    # 보라색 칸 개수
    result = 0
    # 기본 필드 만들어주기 : 10*10
    arr = [[0] * 10 for _ in range(10)]
    
    for i in range(N):
        # 시작점 좌표 (r1, c1), 끝점 좌표 (r2, c2), 색상 정보 color
        r1, c1, r2, c2, color = map(int, input().split())
        # 격자에 빨간색이면 +1,  파란색이면 +2 : 보라색은 3
        for i in range(r1, r2 + 1): 
            for j in range(c1, c2 + 1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc} {result}')
   

# 강사님 답
# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     # board = [[0] * 10] * 10
#     board = [[0 for _ in range(10)] for _ in range(10)]
    
#     for i in range(N):
#         color_data = list(map(int, input().split()))

#         left_top_x = color_data[0]
#         left_top_y = color_data[1]
#         right_bottom_x = color_data[2]
#         right_bottom_y = color_data[3]
#         color = color_data[4]

#         # 색칠시작
#         for x in range(left_top_x, right_bottom_x+1):
#             for y in range(left_top_y, right_bottom_y+1):
#                 board[x][y] += color

#     count = 0

#     for x in range(len(board)):
#         for y in range(len(board[0])):
#             if board[x][y] == 3:
#                 count += 1

#     print(f'#{tc} {result}')
