import sys
sys.stdin = open('input.txt')

# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

numbers = list(range(1,201))

result=[]

for number in numbers:
    if number % 7 == 0 and number % 5 != 0:
        result.append((str(number)))

print(','.join(result))

# join 함수는 string을 연결시 사용하는 함수이므로 숫자를 문자열화 해준 후 사용해야 함.