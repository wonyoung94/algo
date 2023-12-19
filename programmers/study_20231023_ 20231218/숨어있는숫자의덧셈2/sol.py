
# 문자열 my_string이 매개변수로 주어집니다. 
# my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    my_num = []
    c_number = ''

    for char in my_string:
        # char이 문자인지 확인
        if char.isdigit():
            # 숫자면 c_number에 넣기
            c_number += char
        else:
            # 글자면 넘어갈 수 있게 쓰는 경우
            if c_number:
                my_num.append(int(c_number))
                c_number = ''

    if c_number:
        my_num.append(int(c_number))
    else:
        answer = 0

    answer = sum(my_num)
    return answer


print(solution("aAb1B2cC34oOp")) #37
print(solution("1a2b3c4d123Z")) #133


# re 함수를 사용하는데 사실 잘 모르겠음

# import re

# def solution(my_string):
#     return sum([int(i) for i in re.findall(r'\d+', my_string)])

# 한솔이 답변
# def solution(my_string):
#     stack = []
#     for i in range(len(my_string)):
#         if my_string[i].isdigit():
#             # 스택이 비었을 때 - 추가
#             if len(stack) == 0:
#                 stack.append(my_string[i])
#                 idx = i # 인덱스 저장하고 붙어있는 숫자인지 판단할 때 사용
            
#             # 스택이 차있을 때 -     
#             else:
#                 # 현재 인덱스 번호와 추가한 숫자 인덱스 번호 차이가 1이라면(붙어있다면)
#                 if i - idx == 1:
#                     stack[-1] = stack[-1] + my_string[i]
#                     idx = i
#                 # 붙어있는 숫자가 아니라면 
#                 else:
#                     stack.append(my_string[i])
#                     idx = i

#     stack = map(int, stack)
#     return sum(stack)

# 민정이 답
# def solution(my_string):
#     sum_num = 0
    
#     for i in my_string:
#         if not i.isdigit():        # my_string의 글자하나씩 출력해서 그것이 숫자가 아니라면
#             my_string = my_string.replace(i, ' ')  #공백으로 대체해준다

#     for j in my_string.split():     # 공백으로 잘라주고
#         sum_num += int(j)           # mystring 값이 문자이므로 정수형태로 변환하여 더해준다
        
#     return sum_num

# print(solution("aAb1B2cC34oOp"))