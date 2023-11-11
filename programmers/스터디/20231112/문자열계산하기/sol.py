
# my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
# 문자열 my_string이 매개변수로 주어질 때, 
# 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

# 내장함수 있을 것 같은디?

def solution(my_string):
    return eval(my_string)

print(solution("3 + 4")) #7

# 실제 현장에서 eval 함수를 쓰는건 보안에 취약할 수 있어서 쓰지 않는것을 권장
# eval 함수를 실제로 구현 했을때 나오는 함수
# def solution(my_string):
#     return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))