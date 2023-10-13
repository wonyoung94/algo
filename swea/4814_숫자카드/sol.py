import sys
sys.stdin = open('input.txt')

# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

T = int(input())

for tc in range(1, T+1):
    # N: 카드장수, numbers: 카드배열
    
    N = int(input())

    numbers = input() #0이 있어서 그대로 문자열로 사용

    counter = [0 for i in range(10)] # 동일한 의미 counter = [0] * 10 

    for num in numbers:
        counter[int(num)] += 1 #현재 나온 숫자는 문자열이라 int형 변환 필요 

    card_count = 0
    card_number = 0

    for idx, value in enumerate(counter):
        if card_count <= value:
            card_count = value
            card_number = idx

    print(f'#{tc} {card_number} {card_count}')