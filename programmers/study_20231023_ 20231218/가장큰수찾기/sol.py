# 정수 배열 array가 매개변수로 주어질 때,
# 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    max_value = max(array)
    max_index = array.index(max_value)
    answer = [max_value, max_index]
    return answer

print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))


# 내가 하려다 실패한 코드의 정답
# def solution(array):
#     return [max(array), array.index(max(array))]

# sorted 정렬을 통한 코드
# def solution(array):
#     return sorted([[a, i] for i, a in enumerate(array)])[::-1][0]