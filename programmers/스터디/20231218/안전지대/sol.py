
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 
# board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 
# 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# def solution(board):
#     answer = 0
#     for i, j in range(board):
#         if board == 1:
#             board[[i-1]:[i+1]:[j-1]:[j+1]] += 1
    
#     answer = board.count(0)
#     return answer


def solution(board):
    answer = 0
    # board 크기 확인
    rows, cols = len(board), len(board[0])

    # board를 for문을 돌려 1 찾기
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                continue
            
            # 안전지대를 체크할 변수 선언
            count = 0

            # 지뢰 근처의 범위 설정(max, min 한 이유는 out of range 를 피하기 위함)(이게 되네..?)
            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    # 그 범위에 맞게 확인 후 count
                    count += board[x][y]
            # 지뢰의 범위가 닿지 않는 곳은 0이므고 그 갯수를 answer에 append
            if count == 0:
                answer += 1

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))  # 16
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))  # 13
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))  # 0

# 깔끔한 코드
# def solution(board):
#     n = len(board)
#     danger = set()
#     for i, row in enumerate(board):
#         for j, x in enumerate(row):
#             if not x:
#                 continue
#             danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
#     return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)