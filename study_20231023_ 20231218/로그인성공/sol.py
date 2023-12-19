
# 머쓱이는 프로그래머스에 로그인하려고 합니다. 
# 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 
# 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 
# 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

# 회원들의 아이디는 문자열입니다.
# 회원들의 아이디는 알파벳 소문자와 숫자로만 이루어져 있습니다.
# 회원들의 패스워드는 숫자로 구성된 문자열입니다.
# 회원들의 비밀번호는 같을 수 있지만 아이디는 같을 수 없습니다.
# id_pw의 길이는 2입니다.
# id_pw와 db의 원소는 [아이디, 패스워드] 형태입니다.
# 1 ≤ 아이디의 길이 ≤ 15
# 1 ≤ 비밀번호의 길이 ≤ 6
# 1 ≤ db의 길이 ≤ 10
# db의 원소의 길이는 2입니다.

def solution(id_pw, db):
    answer = ''

    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in [row[0] for row in db] or id_pw[1] not in [row[1] for row in db]: 
        # and를 or 로 바꾼 이유 : db[1]의 ID와 db[2] PW 가 같을 경우를 제외하기 위해서
        answer = 'wrong pw'
    elif id_pw not in db:
        answer = 'fail'

    return answer

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])) #"login"
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])) #"wrong pw"
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])) #"fail"

# 대입표현식 기능 사용 : ':=' 이렇게 생긴 연산자(python3.8부터 사용 가능) - 한국어로는 바다코끼리 연산자로불림(커여워...)
# 바다코끼리 연산자의 목적 : 표현식에 이름을 부여하고 재사용 할 수 있게 하는 것
# 더 궁금할 경우 참고
# https://int-i.github.io/python/2020-05-29/python-walrus-operator/
# def solution(id_pw, db):
#     if db_pw := dict(db).get(id_pw[0]):
#         return "login" if db_pw == id_pw[1] else "wrong pw"
#     return "fail"

# 이해하기 쉬운 코드라 긁어옴
# def solution(id_pw, db):
#     answer = ''
#     a, b = id_pw[0], id_pw[1]
#     for pk, pw in db:
#         if pk == a and pw == b:
#             return "login"
#     for pk, pw in db:
#         if pk == a:
#             return "wrong pw"
#     return "fail"