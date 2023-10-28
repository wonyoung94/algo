
# 정수 num과 k가 매개변수로 주어질 때, 
# num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 
# 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

def solution(num, k):
    str_num = str(num)
    if str_num.find(str(k)) != -1:
        return int(str_num.index(str(k)))+1
    else:
        return -1



print(solution(29183, 1)) #3
print(solution(232443, 4)) #4
print(solution(123456, 7)) #-1

# 네 다음 변태
# def solution(num, k):
#     return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

# 생각이 안나서 못썼던 enumerate 함수
# def solution(num, k):
#     for i, n in enumerate(str(num)):
#         if str(k) == n:
#             return i + 1
#     return -1