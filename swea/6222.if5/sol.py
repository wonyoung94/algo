import sys
sys.stdin = open('input.txt')

# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다

char = input()

# 알파벳인지 확인하는 함수 : isalpha
if char.isalpha():

# 소문자인 경우 : 소문자인지 확인하는 함수 islower
    if char.islower():
        result = char.upper()
# 대문자인 경우
    else:
        result = char.lower()
else:
    print(char)

# 아스키코드 변환 함수 ord()
print(ord(char), ord(result)) 

# 최종 출력
print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')