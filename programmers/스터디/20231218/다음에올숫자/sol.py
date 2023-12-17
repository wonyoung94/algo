
# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 
# 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

def solution(common):
    answer = 0
    # 등차수열일 경우
    if common[2] - common[1] == common[1] - common[0]:
        answer = common[-1] + (common[2] - common[1])
    # 등비수열일 경우
    else:
        answer = common[-1] * (common[2] / common[1])
    return answer

print(solution([1, 2, 3, 4])) #5
print(solution([2, 4, 8])) #16

# 다 비슷한 답변이라 PASS