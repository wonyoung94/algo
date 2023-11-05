
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

# 민정이 답
# def solution(array, n):
#     result = []                     # 17, 10 ,10
#     array = sorted(array)           # sorted를 했기 때문에 알아서 더 작은 값이 반환
#     for i in array:                 # 3, 10 ,28 반환
#         result.append(abs(n - i))   # n인 20과의 차이를 절대값을 만들어 result배열에 append
   
    
#     ans = result.index(min(result))  # result의 최소값의 인덱스 반환
#     return array[ans]     

        
# print(solution([3, 10, 30], 20))

# 한솔이 답
# def solution(array, n):
#     answer = 100
#     for num in array:
#         if abs(num - n) < abs(answer - n):
#             answer = num
#         elif abs(num - n) == abs(answer - n):
#             answer = min(num, answer)
#     return answer