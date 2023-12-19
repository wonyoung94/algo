
# 프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다.
# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다.
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eat = coupon//10 
        answer += eat 
        coupon = coupon%10 + eat 
    return answer 


print(solution(100)) #11
print(solution(1081)) #120
print(solution(1999)) #222



# 1081마리를 주문하면 쿠폰이 1081장 발급되므로 서비스 치킨 108마리를 주문할 수 있습니다. 그리고 쿠폰이 1장 남습니다.
# 108마리를 주문하면 쿠폰이 108장 발급되므로 서비스 치킨 10마리를 주문할 수 있습니다. 그리고 쿠폰이 8장 남습니다.
# 10마리를 주문하면 쿠폰이 10장 발급되므로 서비스 치킨 1마리를 주문할 수 있습니다.
# 1마리를 주문하면 쿠폰이 1장 발급됩니다.
# 가지고 있는 쿠폰이 총 10장이므로 서비스 치킨 1마리를 추가로 주문할 수 있습니다.
# 따라서 108 + 10 + 1 + 1 = 120 을 return합니다.

# 뭐야 이거..
# def solution(chicken):
#     return int(chicken*0.11111111111)

# 나만 어렵지 또 
# def solution(chicken):
#     answer = (max(chicken,1)-1)//9
#     return answer

# 민정이와의 고통파티
# def solution(chicken):
#     coupon = 0
#     service_chicken = 0
#     left_coupon = 0
#     sum_coupon = []
#     s_c = 0
#     answer = []
#     while chicken > 0:
#         coupon = chicken
#         service_chicken = chicken // 10
        
#         left_coupon = coupon - (service_chicken*10)
#         sum_coupon.append(left_coupon)
#         chicken = service_chicken
        
#         answer.append(service_chicken)
        
#         s_c += left_coupon
        
#     while s_c >= 10:
#         service_chicken= s_c // 10
#         answer.append(service_chicken)
#         s_c = s_c - (service_chicken *10)
#         s_c += service_chicken

#     return sum(answer)

# print(solution(1999)) #222