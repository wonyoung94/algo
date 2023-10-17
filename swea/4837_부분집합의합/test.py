numbers = list(range(1, 5)) # [1, 2, 3, 4]

n = len(numbers) # n = 4

# 모든 집합의 경우의 수
for i in range(2**n) # 2 ^ n = 2 ** n = 1 << n
# 여기 있는 부분집합의 갯수만큼 반복문을 돌리겠다는 의미
    
    temp = []
    for j in range(n):
        if i & (1<<j): 
        # i와 1<<j를 비교(해당 자리에 숫자가 있는지 없는지 확인?)
        # ex. 0111 & 0001, 0010, 0100, 1000 각각 있나요? 확인 하고 결론 : TTTF - 어떤 데이터가 append되는지 확인 필요
            temp.append(numbers[j])
        
