
# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
# 자연수 n이 매개변수로 주어질 때 
# n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    
    # 1부터 n까지 일단 합성수가 있는지 파악하기
    def divisor(num):
        # 1 ~ 3은 일단 무시하기
        if num < 4:
            return False

        # 1로는 무조건 나눠지니까 2로 나눠지는지부터 확인해보고 나눌 수 있는지 확인
        # 나눠진다면 합성수 (약수가 있음)        
        for i in range(2, num):
            if num % i == 0:
                return True
        
        # 기본값 자체는 False 반환, 합성수가 없을 수는 있지만, 소수가 없을 수는 없기 때문에(n = 1~3)
        return False

    # 합성수가 있는지 파악하고 그 갯수를 세기 위한 변수 count
    count = 0

    # 1부터 3까지는 합성수가 X, 4부터 divisor 함수 for문 돌리기
    for number in range(4, n + 1):  
        if divisor(number):
            count += 1

    return count

print(solution(10)) #5
print(solution(15)) #8

# 너무 깔끔한 답변, 컴파일 시간까지 고려한 답변
# def solution(n):
#     output = 0
#     for i in range(4, n + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 output += 1
#                 break
#     return output
