import sys
sys.stdin = open('input.txt')

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

T = int(input())
answer = 0

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split())) #input을 가져와서 모두 숫자로 바꾼 후 리스트화

    # print(numbers)

# # sort를 이용해서 처리
# sorted(numbers)
# answer = numbers[0] - numbers[-1]

# print(f'#{tc} {answer}')

# # sort가 아닌 방법으로 처리
# answer = max(numbers) - min(numbers)
# print(f'#{tc} {answer}')
# # 이거밖에 생각 안남...

    min_number = 10000000
    # min_number = numbers[0]
    max_number = 0
    # max_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number
        
        if max_number < number:
            max_number = number

    result = max_number - min_number

    print(f'#{tc} {result}')




