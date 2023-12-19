
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

# 큐 원리인가?
# right면 그냥 마지막 숫자 맨 왼쪽 삽입
# left면 그냥 첫 숫자 맨 오른쪽 삽입 하면 안되나


def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers.pop(-1))
    else:
        numbers.append(numbers.pop(0))
        
    return numbers


print(solution([1, 2, 3],"right")) # [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6],"left")) # [455, 6, 4, -1, 45, 6, 4]

# 변태 답변
# def solution(numbers, direction):
#     return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

# 큐 함수를 이용한 방법
# from collections import deque

# def solution(numbers, direction):
#     numbers = deque(numbers)
#     if direction == 'right':
#         numbers.rotate(1)
#     else:
#         numbers.rotate(-1)
#     return list(numbers)

# appendleft : 왼쪽에 개체를 추가합니다.
# extendleft : 왼쪽에 리스트를 연장합니다.
# maxlen : 큐의 길이를 반환합니다.
# popleft : 큐의 맨 왼쪽에 있는 개체를 반환합니다.
# rotate : 큐를 회전합니다.
# https://puleugo.tistory.com/45