
# 선분 3개가 평행하게 놓여 있습니다. 
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
# 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

def solution(lines):
    answer = 0
    # 리스트를 튜플로 정렬
    for i in range(len(lines)):
        lines[i] = tuple(sorted(lines[i]))

    # 겹치는 부분 체크
    for j in range(-100, 101):
        count = 0
        for line in lines:
            if line[0] < j and line[1] >= j:
                count += 1
        # 선이 2개 이상 되면 answer에 append
        if count >= 2:
            answer += 1

    return answer

print(solution([[0, 1], [2, 5], [3, 9]])) #2
print(solution([[-1, 1], [1, 3], [3, 9]])) #0
print(solution([[0, 5], [3, 9], [1, 10]])) #8

# 깔끔하고 수학적 접근(집합)으로 해결

# def solution(lines):
#     s1 = set(i for i in range(lines[0][0], lines[0][1]))
#     s2 = set(i for i in range(lines[1][0], lines[1][1]))
#     s3 = set(i for i in range(lines[2][0], lines[2][1]))
#     return len((s1 & s2) | (s2 & s3) | (s1 & s3))

# 힙 알고리즘으로 풀이 : 뭐라는거야....
# from heapq import heapify, heappop,heappush

# def solution(lines):
#     """
#     condition
#     lines [-99,99] => -1 ~ 2 = 3, -99 ~99 = 198
#     """
#     # (rs,re),(gs,ge),(bs,be) = lines
#     # print(rs,re)
#     answer = 0
#     offset = 99
#     line = [0]*198
#     for s,e in lines:
#         s,e = min(s,e),max(s,e)
#         for i in range(s+offset,e+offset):
#             line[i] +=1

#     for l in line:
#         if l >1:
#             answer+=1
#     print(line)
#     print(answer)
#     return answer

# def solution(lines):
#     answer = 0

#     for i in range(len(lines)):
#         lines[i].sort()

#     for j in range(-100,101):
#         count=0
#         for i in range(len(lines)):
#             if lines[i][0] < j and lines[i][1] >= j:
#                 count+=1

#         if count>=2:
#             print(j)
#             answer+=1

#     return answer

