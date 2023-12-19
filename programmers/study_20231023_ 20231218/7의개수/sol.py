
# 머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 
# 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.



def solution(array):

    #스트링으로 합치고 7 갯수 카운트 가능한가?
    a_str = ''.join(map(str, array))
    answer = a_str.count('7')
    return answer


print(solution([7, 77, 17])) #4
print(solution([10, 29])) #0

# 짧게 쓰면 이렇게 됨
# def solution(array):
#     return str(array).count('7')

# count 함수 안쓰고 세는 법
# def solution(array):
#     answer = 0
#     for i in array:
#         for j in str(i):
#             if j == '7':
#                 answer += 1
#     answer

#     return answer
