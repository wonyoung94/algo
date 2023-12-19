
# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 
# 정수 i, j, k가 매개변수로 주어질 때, 
# i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

def solution(i, j, k):
    num = list(map(str, range(i,j+1)))
    letter = ''.join(num)
    str_k = str(k)
    answer = letter.count(str_k)
    return answer

    #i부터 j까지 join str 해서 다 합쳐버린다음에 k 카운트


print(solution(1, 13, 1)) #6
print(solution(10, 50, 5)) #5
print(solution(3, 10, 2)) #0

# 내가 한 방법을 줄여 쓰면 이렇게 됨.
# def solution(i, j, k):
#     answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
#     return answer
