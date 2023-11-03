
# 정수 배열 array와 정수 n이 매개변수로 주어질 때, 
# array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

def solution(array, n):

    # array에 n을 넣고 sorted 한다음에 양옆의 값을 비교
    array.append(n)
    n_array = sorted(array)
    n_index = n_array.index(n)

    # n의 인덱스 값이 0 or -1 이면 1, -2 출력
    if n_index == 0:
        return n_array[1]

    elif n_index == len(n_array)-1:
        return n_array[-2]

    # n보다 작은수, n, n보다 큰 수를 비교해서 더 작은 값 출력
    else:
        if n_array[n_index+1] - n < n - n_array[n_index-1]:
            return n_array[n_index+1]

        # 작으면, n보다 작은 수 출력
        else:
            return n_array[n_index-1]
        

print(solution([1, 9], 5)) #1
print(solution([3, 11, 28], 20)) #28
print(solution([10, 11, 12], 13)) #12

# abs 하다가 실패했는데 이걸 한줄로 해버리네...속상..
# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

# 나도...abs 쓰고 싶었는데...ㅎ
# def solution(array, n):
#     answer = []
#     m = 99999999
#     array.sort()
#     for a in array:
#         # print(abs(a-n), m)
#         if abs(a - n) < m:
#             m = abs(a-n)
#             answer = a
#     return answer