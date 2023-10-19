import sys
sys.stdin = open('input.txt')

T = int(input())

# 스텍에 한글자씩 넣는다고 생각한다
# C를 넣고 A를 넣고 A를 넣으면 같은거라 지우고
# C만 남은 상태에서 A를 또 넣고 
# 그다음에 B를 넣고 
# C A B 가 있는데 거기서 또 B가 들어오면 맨 위의 B랑 나가고 
# 마지막 A가 들어오면 남아있던 C A 중 위에 있는 A와 나가서 
# C만 남아있는다 

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()

    stack = []

    for char in string:
        # 스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(char)
        # 스택이 비어있지 않은경우 => 비교를 할 수 있는 상태
        else:
            # 제일 마지막 데이터와 비교하는 데이터가 일치하는경우
            if char == stack[-1]:
                stack.pop()
            # 일치하지 않은경우
            else:
                stack.append(char)

    print(stack)