#정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

def solution(n):
    answer = 0
    r_list=[]
    #숫자를 문자로 만든다
    n_str = str(n) #'1234'는 공백이 없어서 split 실행 불가능
    #바로 map함수를 이용해 list에 넣는다
    r_str=list(map(int, n_str))
    #for문으로 모든 데이터를 합친다.
    for i in r_str:
        answer += i
    return answer
print(solution(1234))

# def solution(n):
#     answer = 0

#     for i in str(n):
#         answer += int(i)

#     return answer
# print(solution(1234))


# 수학적 접근

# def solution(n):
#     answer = 0

#     while n > 0:
#         # a : 몫, b : 나머지
#         a = n // 10
#         b = n % 10

#         n = a
#         answer +=b
#     return answer

# print(solution(1234))
