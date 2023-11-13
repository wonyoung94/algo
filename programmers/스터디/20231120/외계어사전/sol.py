
# PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 
# 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
    #dic의 요소를 돌면서 spell for문 돌면서 다 있는지 확인

def solution(spell, dic):
    for word in dic:
        find = []
        for char in spell:
            if word.find(char) != -1:
                find.append(1)
            else:
                find.append(0)
                break
        if 0 not in find:
            return 1
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))  # 2
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))  # 2


# 지리는 답 : 문제는 중복데이터가 없고, set는 순서도 없는 특성을 이용
# def solution(spell, dic):
#     spell = set(spell) # spell을 일단 set로 바꿔라!
#     for s in dic: # dic을 돌면서 set를 확인
#         if not spell-set(s): # dic의 값을 set화 한 값이랑 spell의 set 값이 같으면 
#             return 1 # 1을 반환
#     return 2 # 아니면 2를 반환

# sorted를 이용한 답변
# def solution(spell, dic):
#     for d in dic:
#         if sorted(d) == sorted(spell):
#             return 1
#     return 2
