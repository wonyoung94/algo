
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 
# 연속된 수 num개를 더한 값이 total이 될 때, 
# 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

def solution(num, total):
    return list(range(int((((total*2)/num) + 1 - num)/2), int((((total*2)/num) + 1 - num)/2) + num))

print(solution(3, 12)) #[3, 4, 5]
print(solution(5, 15)) #[1, 2, 3, 4, 5]
print(solution(4, 14)) #[2, 3, 4, 5]
print(solution(5, 5)) #[-1, 0, 1, 2, 3]

# 중앙값을 이용한 풀이방식
# def solution(num, total):
#     answer = []
#     if num%2==0:
#         newnum = (total//num)-(num//2)+1
#     else:
#         newnum = (total//num)-(num//2)
#     for i in range(num):
#         answer.append(newnum+i)
#     return answer

