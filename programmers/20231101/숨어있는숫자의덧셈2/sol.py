
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