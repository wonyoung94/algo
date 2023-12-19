
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. 
# a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

def solution(age):
        universe = str.maketrans('0123456789', 'abcdefghij')
        answer = str(age).translate(universe)
        return answer


# 우리 머쓱이 이젠 우주여행도 하네 부자야..
# age는 int 형 데이터 - str 데이터로 변경 
# 리스트 구성 후 조건문 형성 
# join 함수를 써서 result 
# 포기

# translate 함수 사용

print(solution(23)) # cd
print(solution(51)) # fd
print(solution(100)) # baa

# 내가 굳이 하려고 했던걸 하려면...이렇게 해야 하네....
# def solution(age):
#     age = str(age)
#     age = age.replace("0", "a")
#     age = age.replace("1", "b")
#     age = age.replace("2", "c")
#     age = age.replace("3", "d")
#     age = age.replace("4", "e")
#     age = age.replace("5", "f")
#     age = age.replace("6", "g")
#     age = age.replace("7", "h")
#     age = age.replace("8", "i")
#     age = age.replace("9", "j")
#     return age

# 실제 내가 실행한 코드를 강제로 미친듯이 짧게 하면 이렇게 됨...
# solution=lambda age:str(age).translate(str.maketrans('0123456789','abcdefghij'))


# 한솔이 답변
# 알파벳 정렬하는 함수 이용하기 위해 import 
# from string import ascii_lowercase

# def solution(age):
#     # 알파벳 리스트 만들고 그 인덱스에 해당하는 값 문자열형태로 더하기
#     answer = ''
#     alpha = list(ascii_lowercase)

#     age = str(age)
#     for char in age:
#         answer += alpha[int(char)]
#     return answer