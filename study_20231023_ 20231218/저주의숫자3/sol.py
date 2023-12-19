# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 
# 3x 마을 사람들의 숫자는 다음과 같습니다.

# 정수 n이 매개변수로 주어질 때, 
# n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

def solution(n):
    x = [i for i in range(1, 200) if i % 3 != 0]
    y = [i for i in range(1, 200) if '3' not in str(i)]

    answer = list(set(x) & set(y))
    return answer[n-1]

print(solution(15)) #25
print(solution(40)) #76
print(solution(100)) #185

# 진짜 이정도면....
# def solution(n):
#     answer = [0, 1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29, 40, 41, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 74, 76, 77, 79, 80, 82, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 101, 104, 106, 107, 109, 110, 112, 115, 116, 118, 119, 121, 122, 124, 125, 127, 128, 140, 142, 145, 146, 148, 149, 151, 152, 154, 155, 157, 158, 160, 161, 164, 166, 167, 169, 170, 172, 175, 176, 178, 179, 181, 182, 184, 185]
#     return answer[n]

# 깔끔한 코드 :(한솔이 코드)
# def solution(n):
#     answer = 0
#     for _ in range(n):
#         answer += 1
#         while answer % 3 == 0 or '3' in str(answer):
#             answer += 1
#     return answer

# 내가 쓴거 줄인 코드 : 하지만 리스트를 작성해서 메모리를 많이 낭비해 비효율
# def solution(n):
#     return [i for i in range(200) if i % 3 != 0 and '3' not in str(i)][n-1]

# 민정이 코드
# def solution(n):
#     a = []
#     for i in range(1, 250):
#         if i % 3 != 0 and '3' not in str(i):
#             a.append(i)

#     answer = {}
#     # answer = {key+1: value for key, value in enumerate(a)}

#     for key, value in enumerate(a):
#         answer[key+1] = value 

#     return answer[n]
    
# print(solution(15))