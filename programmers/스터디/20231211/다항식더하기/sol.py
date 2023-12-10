
# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 
# 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.

def solution(polynomial):
    answer = list(polynomial.replace(' ', ''))
    #['3', 'x', '+', '7', '+', 'x']
    # ['x', '+', 'x', '+', 'x']

    # x 앞에 숫자가 없으면 1을 넣어줘라
    i = 0
    while i < len(answer):
        if answer[i] == 'x' and (i == 0 or not answer[i-1].isdigit()):
            answer.insert(i, '1')
        i += 1
    # ['3', 'x', '+', '7', '+', '1', 'x']
    # ['1', 'x', '+', '1', 'x', '+', '1', 'x']

    # 숫자 뒤에 x 가 있는 수를 x, 숫자 뒤에 x가 없는 수를 y로 할당
    x = []
    y = []
    a = 0
    while a < len(answer):
        if answer[a] == 'x':
            x.append(int(answer[a-1]))
        else:
            y.append(answer[a-1])
        a += 1
    
        # x에 숫자가 있는거만 추출
        if x == []:
            int_x = 0
        else:
            int_x = int(sum(x))
        # y에 숫자가 있는거만 추출
        y = [num for num in y if num.isdigit()]
        if y == []:
            int_y = 0
        else:
            int_y = int(sum(y))
        # list comprehension으로 목록의 숫자 추출
        # if로 분기처리 : 숫자가 없으면 0으로 처리 

    if int_x == 0 and int_y !=0:
        answer = str(int_y)
    elif int_x != 0 and int_y == 0:
        answer = f"{int_x}x"
    else:
        answer = f"{int_x}x + {int_y}"

    return answer

print(solution("3x + 7 + x")) #"4x + 7"
print(solution("x + x + x")) #"3x"
print(solution("7x + 4 + 9 + 5x")) #"12x + 13"
print(solution("10x")) #"10x"
#########################################################
# 스터디 하면서 이거 고쳐보기

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






