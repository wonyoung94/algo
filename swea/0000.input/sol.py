import sys
sys.stdin = open('input.txt')

TC = int(input()) 

# Test Case의 약자 
# input으로 가져온 데이터는 글자 데이터로 인식하므로 int화 해야 함.

for i in range(TC):
    num = int(input())

    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')


#1차원 리스트 input 받기

# numbers = input().split()
#   print(numbers)
#   print(type(numbers))

# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')

numbers = list(map(int, input().split()))
print(numbers)
# map함수는 두가지 인자가 필요
# 데이터타입, 함수

for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다.')