
# 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, 
# my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 
# return 하도록 solution 함수를 완성해보세요.

def solution(my_string):
    answer = []
    for char in my_string:
        if not char.islower():
            answer.append(char.lower())
        else:
            answer.append(char) # answer += char

    answer = ''.join(sorted(answer))
    return answer



print(solution("Bcad")) #"abcd"
print(solution("heLLo")) #"ehllo"
print(solution("Python")) #	"hnopty"

# 고인물
# def solution(my_string):
#     return ''.join(sorted(my_string.lower()))

# 무난하게 깔끔해서 들고옴(가독성 b)
# def solution(my_string):
#     answer = my_string.lower()
#     answer = ''.join(sorted(answer)) 
#     return answer



