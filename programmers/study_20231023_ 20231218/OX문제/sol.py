
# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다. 
# 단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.
# 1 ≤ quiz의 길이 ≤ 10
# X, Y, Z는 각각 0부터 9까지 숫자로 이루어진 정수를 의미하며, 
# 각 숫자의 맨 앞에 마이너스 기호가 하나 있을 수 있고 이는 음수를 의미합니다.
# X, Y, Z는 0을 제외하고는 0으로 시작하지 않습니다.
# -10,000 ≤ X, Y ≤ 10,000
# -20,000 ≤ Z ≤ 20,000
# [연산자]는 + 와 - 중 하나입니다.

def solution(quiz):
    result = []
    answer = []
    for char in range(len(quiz)):
        result.append(quiz[char].split('='))
    # [['3 - 4 ', ' -3'], ['5 + 6 ', ' 11']]
    for i, j in result:
        if eval(i.strip()) == int(j.strip()):
            answer.append('O')
        else:
            answer.append('X')
    # print(result) = [['3 - 4 ', ' -3'], ['5 + 6 ', ' 11']]
    # print(answer) = ['X', 'O']
    
    return answer

# eval 함수를 쓰지 않고 해결 해보기 - 해결은 되지만 런타임오류 : 항이 3개가 아닐때도 해결 가능
# def solution(quiz):
#     result = []
#     answer = []
    
#     for question in quiz:
#         # 똑같이 quiz 요소를 = 을 기준으로 나눠줌
#         solve, result = question.split('=')
#         solve = solve.strip()
#         result = int(result.strip())
        
#         # 연산자가 없을 경우 그자리에서 break
#         operator = None 
#         for char in solve:
#             if char in ('+', '-'):
#                 operator = char
#                 break

#         # 연산자가 있을 경우 계산
#         if operator:
#             num1, num2 = map(int, solve.split(operator))
#             cal_result = num1 + num2 if operator == '+' else num1 - num2

#             if cal_result == result:
#                 answer.append('O')
#             else:
#                 answer.append('X')
#         else:
#             # 연산자가 없을 경우
#             if result == int(char):
#                 answer.append('O')
#             else:
#                 answer.append('X')

#     return answer

# eval 함수 안썼을때 eval 함수를 대체할 수 있는 새로운 함수를 구현 후 계산 : 
# def calculate(equation):
#     parts = equation.split()
#     이 문제에 국한된 코드 : X, Y, Z 항이 3개로 주어졌으므로 그 이외의 상황은 제외 - 없어도 문제에 상관X
#     if len(parts) != 3:
#         return None  
#     num1, operator, num2 = map(str.strip, parts)
#     if operator == '+':
#         return int(num1) + int(num2)
#     elif operator == '-':
#         return int(num1) - int(num2)
#     이 문제에 국한된 코드 : 연산자가 +, -가 아닌 상황은 제외 - 없어도 문제에 상관X
#     else:
#         return None

# def solution(quiz):
#     answer = []

#     for question in quiz:
#         equation, solve = map(str.strip, question.split('='))
#         result = calculate(equation)

#         if result == int(solve):
#             answer.append('O')
#         else:
#             answer.append('X')

#     return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"])) #["X", "O"]
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])) #["O", "O", "X", "O"]

# 새로운 함수를 따로 구현하지 않고 런타임에러 없는 식
# def solution(quiz):
#     answer = []
#     for q in quiz:
#         L,R = q.split(' = ')
#         a,op,b = L.split()
#         if op=='+':
#             result = 'O' if int(a)+int(b)==int(R) else 'X'
#             answer.append(result)
#         else:
#             result = 'O' if int(a)-int(b)==int(R) else 'X'
#             answer.append(result)
#     return answer

