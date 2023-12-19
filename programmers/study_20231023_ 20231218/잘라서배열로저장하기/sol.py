
# 문자열 my_str과 n이 매개변수로 주어질 때, 
# my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(my_str, n):
    answer = []
    i = 0
    while i < len(my_str):
        substring = my_str[i:i+n]
        answer.append(substring)
        i += n
    return answer

print(solution("abc1Addfggg4556b", 6)) # ["abc1Ad", "dfggg4", "556b"]
print(solution("abcdef123", 3)) # ["abc", "def", "123"]

# 슬라이싱은 out of range가 없음
# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]