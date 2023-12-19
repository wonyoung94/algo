
# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 
# 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.

def solution(polynomial):
    # 문자 쪼개기
    polynomial = polynomial.replace(' ', '')
    polynomial = polynomial.split('+')

    # x 앞에 숫자가 없으면 1을 넣어줘라
    i = 0
    while i < len(polynomial):
        if polynomial[i] == 'x' :
            polynomial[i] = '1x'
        i += 1

    # 숫자 뒤에 x 가 있는 수를 x, 숫자 뒤에 x가 없는 수를 y로 할당
    x = []
    y = []
    
    for char in polynomial:
        if char[-1] == 'x':
            x.append(int(char[:-1]))
        else:
            y.append(int(char))

    # ([3, 1], [7])
    # ([1, 1, 1], [])
    # ([7, 5], [4, 9])
    # ([10], [])

    # if로 분기처리 : 숫자가 없으면 0으로 처리 

    if x == []:
        return f'{sum(y)}'
    if y == []:
        if x == [1]:
            return f'x'
        else:
            return f'{sum(x)}x'
    else:
        if x == [1]:
            return f'x + {sum(y)}'
        else:
            return f'{sum(x)}x + {sum(y)}'


print(solution("3x + 7 + x")) #"4x + 7"
print(solution("x + x + x")) #"3x"
print(solution("7x + 4 + 9 + 5x")) #"12x + 13"
print(solution("10x")) #"10x"
#########################################################
# 스터디 하면서 이거 고쳐보기 : 와 했다..... 한솔이 짱....

# https://somjang.tistory.com/entry/Programmers-%EB%8B%A4%ED%95%AD%EC%8B%9D-%EB%8D%94%ED%95%98%EA%B8%B0-Python
# 그냥 답지 일단 긁어옴

# def solution(polynomial):
#     calc_dict = {}
    
#     # + 기준으로 항 추출
#     for variable in polynomial.split(" + "):
#         # 숫자와 문자로 구성 되어 있는 식일 경우
#         if not variable.isnumeric():
#             variable_name = variable[-1]
#             variable_num = int(variable[:-1]) if variable[:-1] != '' else 1

#             if variable_name not in calc_dict:
#                 calc_dict[variable_name] = 0
#             calc_dict[variable_name] += variable_num

#         # 숫자로만 구성되어있는 식일 경우
#         else:
#             if '' not in calc_dict:
#                 calc_dict[''] = 0
#             calc_dict[''] += int(variable)            
    
#     # 딕셔너리로부터 다항식 형태의 모양으로 return
#     return " + ".join([f"{v if v > 1 else ''}{k}" if k != '' else f"{v}" for k, v in sorted(calc_dict.items(), key=lambda x: x[0], reverse=True)])


# 프로그래머스의 외부 답안지
# def solution(polynomial):
#     number = 0
#     x = 0
#     for char in polynomial.split(" + "):
#         if char.isnumeric():
#             number += int(char)
#         else:
#             x += int(char[:-1] or "1")
#     return " + ".join([
#         *([f"{x if x > 1 else ''}x"] if x else []),
#         *([f"{number}"] if number else []),
#     ])



