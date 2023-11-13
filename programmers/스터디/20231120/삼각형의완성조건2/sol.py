
# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
# 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

# 삼각형이 되기 위한 조건 : a + b >= c
def solution(sides):
    answer = 0
    sides.sort() # sort로 일단 어떤 변이 더 긴지 확인 하기
    min_val, max_val = sides[0], sides[1]
    # sides중에서 가장 큰 변의 길이가 있을 때
    for i in range(max_val - min_val + 1, max_val + 1):
        answer += 1
    # sides중에서 가장 큰 변의 길이가 없을 때 (모르는 변이 가장 클 때)
    for i in range(max_val + 1, max_val + min_val):
        answer += 1

    return answer

print(solution([1, 2])) #1
print(solution([3, 6])) #5
print(solution([11, 7])) #13

# 네? 뭐라고요?
# 삼각현 세 변의 길이 : i, j, x
# i = 아는 길이 중 작은 길이
# j = 아는 길이 중 긴 길이
# x = 모르는 값
# if x가 최대일 경우 
# i + j > x >= j 
#     따라서 i개의 경우의 수 만큼 가능
# if j가 최대일 경우 
# j >= x > j - i 
#     따라서 i개의 경우의 수가 가능하지만 
# if x가 최대일 경우 
#     x == j인 경우의 수가 중복되기 때문에 최종결과에 -1
# 따라서 총 가능한 경우의 수 = 입력 받은 가장 작은 수 * 2 - 1

# 그니까 뭐라고요?
# def solution(sides):
#     return 2 * min(sides) - 1