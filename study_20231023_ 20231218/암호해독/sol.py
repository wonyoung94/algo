# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

# 문자열의 인덱스가 code의 배수인가? = append
# 인덱스 번호 접근 함수

def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if code * i < len(cipher):
            answer += cipher[(code * (i+1))- 1]
        else:
            break   

    return answer

# kattac
# kfallbac
# 출력물 상태 인덱스 -1 나오는거 해결해야함 
# 14줄 answer += cipher[(code * i)- 1]에서 i 를 i+1로 변경
# 프로그래머스 왜 런타임 오류?

def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]
    return answer

def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer

print(solution("dfjardstddetckdaccccdegk",4))
print(solution("pfqallllabwaoclk",2))

# def solution(cipher, code):
#     answer = cipher[code-1::code]
#     return answer

# def solution(cipher, code):
#     return ''.join(cipher[i] for i in range(code-1,len(cipher),code))