import sys
sys.stdin = open('input.txt', encoding='utf-8') 
# 한글 데이터를 끌어올때 필요한 명령어 encording='utf-8'

# 첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.
# 예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.
# 단, 비긴 경우는 Result : Draw 라고 출력한다.

man1 = input()
man2 = input()

rcp = ['가위','바위','보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    print(f'Result : Man{result+3} Win!')