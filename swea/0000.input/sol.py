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


# 2차원 리스트 입력

N = int(input()) # 3 이라는 데이터를 받아옴
matrix = []

for i in range(N):
    numbers = list(map(int, input().split())) #글자 형태로 저장되어있는 데이터를 숫자로 만들어 리스트화
    matrix.append(numbers)

# 데이터 자체를 반복
# for row in matrix:
#     for item in row:
#         print(item)

#행우선 반복(index 접근)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(i, j)

#열우선 반복(index 접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(j, i, matrix[i],[j])