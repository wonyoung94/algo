import sys
sys.stdin = open('input.txt')

T = int(input())

# 스텍 리스트 생성 후 
# 여는 괄호를 해서 
# 일단 넣고
# 그다음에 닫는 괄호를 
# 확인 했을때 
# 짝이 맞으면
# 여는 괄호랑 같이 끄내준다
# 닫는거만 들어오면
# 그냥 쌓는다?
# 이렇게 해서 스택 길이가 0이면 1
# 스택 길이가 1 이상이면 0

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    code = input()

    stack = []

    for char in code:
        if char == '(' or char == '{':
            stack.append(char)
        elif len(stack) and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(result)