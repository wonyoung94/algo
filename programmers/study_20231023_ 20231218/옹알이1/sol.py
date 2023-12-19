
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(babbling):
    baby_able = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    # babbling에서 baby_able의 요소들을 '0'으로 대체
    for i in range(len(babbling)):
        for baby_word in baby_able:
            babbling[i] = babbling[i].replace(baby_word, '0')
            
    # 남은 요소들중에서 숫자로만 이루어진것을 answer에 append (대체를 0으로 ex. '0' - 숫자, '0a' - 숫자 아님)
    for j in range(len(babbling)):
        if babbling[j].isdigit():
            answer +=1    
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))  # 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))  # 3

# 씁 공백으로 하니까 오류나서 숫자 넣어줬는데 
# def solution(babbling):
#     c = 0
#     for b in babbling:
#         for w in [ "aya", "ye", "woo", "ma" ]:
#             b = b.replace(w, ' ', 1)
#         if len(b.strip()) == 0:
#             c += 1
#     return c

# 나만 모르는 re 함수
# import re

# def solution(babbling):
#     regex = re.compile('^(aya|ye|woo|ma)+$')
#     cnt=0
#     for e in babbling:
#         if regex.match(e):
#             cnt+=1
#     return cnt
