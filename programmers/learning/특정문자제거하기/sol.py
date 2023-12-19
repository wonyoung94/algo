# 문자열 my_string과 문자 letter이 매개변수로 주어집니다.
# my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요

# 문자열은 삭제가 불가능

# 삭제해야 하는 항목을 replace를 적용해 공백으로 만들고 공백 삭제

# def solution(my_string, letter):
#     answer = ''
#     # replace를 적용해 공백으로 대체
#     answer = my_string.replace(letter,'')
#     #answer라는 값에 저장 해줘야 함.
#     return answer

def solution(my_string, letter):
    answer = ''

    for string in my_string: # my_string 에서 string을 반복하는데
        if string != letter: # 만약 string이 letter을 포함하고 있지 않으면
            answer += string # answer에 그 string 값을 넣어준다 - 이걸 반복

    return answer


print(solution('abcdef','f'))
print(solution('BCBdbe','B'))