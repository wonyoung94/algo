# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# list 메소드 이용한 방법
# def solution(num_list):
#     answer = []
#     # answer = num_list[::-1]
#     num_list.reverse()
#     answer = num_list
#     return answer

# 이해하면 다른 언어를 활용하기 좋음(다른 언어구조에 맞는 사고)
# def solution(num_list):
#     answer = []
    
#     # for i in range(len(num_list)-1, 0, -1):
#     for i in range(len(num_list)):
#         # num_list[i]
#         # print(i)
#         # print(len(num_list)-i-1)
#         answer.append(num_list[len(num_list)-1-i])

#     return answer

# for문을 통한 방법
def solution(num_list):
    answer = []

    for num in num_list:
        answer.insert(0, num)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))






# num_list = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']

# N = len(num_list)

# for i in range(N):
        
#         answer.append(num_list[N-1-i])


# i : 0 ~ N-1
# N - 1 - i : N-1 ~ 0