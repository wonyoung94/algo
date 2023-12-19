
# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 
# 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(box, n):
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer


# 우리 머쓱이는 항상 일거리를 만들어오더라...
# 박스는 리스트 형태
# 주사위는 int 형 
# 가로 세로 높이를 각각 n으로 나눈 값을 각각 곱해주는 값


print(solution([1, 1, 1], 1)) # 1
print(solution([10, 8, 6], 3)) # 12

# 어차피 모든 value값을 다 해야 하니까 반복문처리
# def solution(box, n):
#     answer = 1
#     for b in box:
#         answer *= b // n
#     return answer

# 람다와 메쓰의 조합
# import math

# def solution(box, n):
#     return math.prod(map(lambda v: v//n, box))

# 깔끔하게 변수 지정
# def solution(box, n):
#     answer = 0
#     a = box[0] // n
#     b = box[1] // n
#     c = box[2] // n
#     return a * b * c