# 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.

# num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 
# num_list를 2 * 4 배열로 다음과 같이 변경합니다. 
# 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.

def solution(num_list, n):
    # i부터 n만큼씩 잘라서 리스트화
    answer = [num_list[i:i+n] for i in range(0, len(num_list), n)]
    return answer




print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2)) # [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3)) # [[100, 95, 2], [4, 5, 6], [18, 33, 948]]



# numpy 라이브러리가 있음

# import numpy as np
# def solution(num_list, n):
#     li = np.array(num_list).reshape(-1,n)
#     return li.tolist()

# 내 방법을 풀어 쓰면 이렇게 됨

# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n):
#         answer.append(num_list[i:i+n])
#     return answer