
# 머쓱이는 RPG게임을 하고 있습니다. 
# 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
# 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1],
# left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
# 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
# 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 
# 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

# [0, 0]은 board의 정 중앙에 위치합니다. 
# 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

# def solution(keyinput, board):
#     answer = [keyinput.count('right') - keyinput.count('left'), keyinput.count('up') - keyinput.count('down')]
#     for i in range(len(answer)):
#         if not - board[i] // 2 < answer[i] < board[i] // 2:
#             if answer[i] > 0:
#                 answer[i] = board[i] // 2
#             else:
#                 answer[i] = - board[i] // 2 +1
#     return answer
# 이렇게 하면 끝에서 끝까지 가는 경우(케이스8), 통과 불가

def solution(keyinput, board):
    limit_x, limit_y = board[0] // 2, board[1] // 2 # 범위 1차 설정
    answer = [0,0] #시작 위치
    
    for i in keyinput: # 정직하게 하나씩 하나씩 이동
        if i == 'right' and answer[0]+1 <= limit_x: # 이동할 공간이 있다면 이동
            answer[0] += 1
        elif i == "left" and answer[0]-1 >= - limit_x:
            answer[0] -= 1
        elif i == 'up' and answer[1]+1 <= limit_y:
            answer[1] += 1
        elif i == 'down' and answer[1]-1 >= - limit_y:
            answer[1] -= 1
    return answer


print(solution(["left", "right", "up", "right", "right"], [11, 11])) # [2, 1]
print(solution(["down", "down", "down", "down", "down"], [7, 9])) # [0, -4]
print(solution(["right", "right", "right", "right", "right", "left"], [9, 5])) # [3, 0]

# 딕셔너리를 이용해 풀기
# def solution(keyinput, board):
#     x_lim,y_lim = board[0]//2,board[1]//2
#     move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
#     x,y = 0,0
#     for k in keyinput:
#         dx,dy = move[k]
#         if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
#             continue
#         else:
#             x,y = x+dx,y+dy

#     return [x,y]