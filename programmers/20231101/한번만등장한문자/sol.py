
# 문자열 s가 매개변수로 주어집니다. 
# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

# 스택 원리로 제거하고 싶은데.... 이거랑 좀 다른것 같은데ㅠㅠㅠㅠ

# 각 문자의 갯수를 세서, 1개이면 answer에 append.

def solution(s):
    answer = ''
    for char in s:
        if s.count(char) == 1:
            answer += char
    return ''.join(sorted(answer))

print(solution("abcabcadc")) # "d"
print(solution("abdc")) # "abcd"
print(solution("hello")) # "eho"



# 내 코드 줄인 사람
# def solution(s):
#     answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
#     return answer

# 한솔이 답
# def solution(s):
#     # s 안에 1개만 있는 문자만 stack에 추가
#     stack = []
#     for char in s:
#         if s.count(char) == 1:
#             stack.append(char)

#         stack.sort() # 문자 순서대로 정렬
#         return ''.join(stack) # 문자열로 출력 

#     # 짧은버전
#     stack = [char for char in s if s.count(char) == 1]
#     stack.sort()
#     return ''.join(stack)