
# 머쓱이는 친구들과 369게임을 하고 있습니다. 
# 369게임은 1부터 숫자를 하나씩 대며 
# 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 
# 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

def solution(order):
    answer = 0
    o_str = str(order)
    
    for char in o_str:
        if char.isdigit() and int(char) != 0 :
            if char.isdigit() and int(char) % 3 == 0 :
                answer += 1

    return answer


# # 3의 배수가 나오면 append 하라 

print(solution(3)) #1
print(solution(29423)) #2

# 한줄장인
# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

# 369게임을 이해 잘 하신 분 
# def solution(order):
#     answer = 0
#     order = str(order)
#     return order.count('3') + order.count('6') + order.count('9')