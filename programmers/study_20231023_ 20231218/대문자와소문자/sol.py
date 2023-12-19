
# 문자열 my_string이 매개변수로 주어질 때, 
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''

    # 문자열은 수정이 안되므로 전체 데이터 재할당이 필요

    for char in my_string:
        if char.isupper() == True:
            answer += char.lower()
        else :
            answer += char.upper()
    return answer

print(solution("cccCCC"))
print(solution("abCdEfghIJ"))

# def solution(my_string):
#     return my_string.swapcase()

# def solution(my_string):
#     return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])