
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 
# 최빈값을 return 하도록 solution 함수를 완성해보세요. 
# 최빈값이 여러 개면 -1을 return 합니다.

def solution(array): 
    a_dict = {}
    max_list = {}
    answer = 0
    # dict에 array 횟수 넣기
    for a in array:
        if a_dict.get(a) is None:
            a_dict[a] = 1 # a라는 숫자가 나올때 1을 삽입
        else:
            a_dict[a] += 1 #a라는 숫자의 빈도 증가
    #여러개의 최빈값을 뽑아내기
    most = max(a_dict.values()) #최빈값 추출 - 값중에 최대값 찾기

    #최빈값 dictionary만들기
    for key, value in a_dict.items():
        if value == most:
            max_list[key] = value

    #dictionary에서 value값 추출하기(2개 이상이면 분기 처리)
    result = [int(key) for key in max_list.keys()]
    if len(result) == 1:
        answer = result[0]
    else:
        answer = -1
    
    return answer

print(solution([1, 2, 3, 3, 3, 4])) #3
print(solution([1, 1, 2, 2])) #-1
print(solution([1])) #1

    
# 왜인지 모르겠는데 또 프로그래머스에 애매하게 작성되어있는게 있어서 이거 수정해서 답 구함


# 제일 핫한 답변이라 들고 옴 : 저용량(input값이 적을 때)일 경우 가장 빠르게 답을 구할 수 있음
# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1

# array.remove(a) 이후 어떻게 빈도수 순으로 array가 정렬되는건가요?
# 정렬을 이용한 방법이 아닙니다. 
# set을 이용하여 배열의 모든 원소를 한 개씩 모두 소거해 나가면서 
# 최종적으로 값의 종류가 1개가 남을 경우(최빈값) i=0이므로 해당 값을 반환하고, 
# 값의 종류가 두 개 이상이 남을 경우 i가 1이상이 되므로 -1을 반환합니다. 
# [3, 3, 3, 1, 2]일때 한 번 반복을 돌면 원소의 종류[1, 2, 3]을 한 번씩 제거하고 [3, 3]이 됩니다. 
# set([3, 3])은 (3)이 되므로 그럼 i는 0에서 끝납니다.


# counter를 사용해 풀 경우, input값이 클 때 빠르게 처리
# from collections import Counter

# def solution(array):
#     a = Counter(array).most_common(2)
#     if len(a) == 1:
#         return a[0][0]
#     if a[0][1] == a[1][1]:
#         return -1
#     return a[0][0]

