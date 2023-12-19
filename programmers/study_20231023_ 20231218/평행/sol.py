
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 
# 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
 
def solution(dots):
    answer = 0
    dots = sorted(dots)
    delta_line1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    delta_line2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    if delta_line1 == delta_line2
        answer = 1
    else:
        answer = 0
    return answer

# 기울기를 이용해 직관적으로 표기

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]])) #1
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]])) #0

# 딱히 맘에드는 답변 없음