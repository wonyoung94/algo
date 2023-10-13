import sys
sys.stdin = open('input.txt')

# baby_gin이 true라면 출력, false라면 pass

# 각각의 숫자가 몇개인지 체크
# 그 숫자들이 연속되어있는지 확인

T = int(input())

for tc in range(1, T+1):
    numbers = input() # 텍스트 파일의 데이터는 아직 글자입니다.

    # counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # List Comprehension 형식
    counter = [0 for i in range(10)] 

    for number in numbers:
        counter[int(number)] += 1 #넘버에 해당하는 카운터를 입력 

    # print(counter) : 전체 카드를 돌면서 몇장씩 있는지 확인

    idx = 0
    is_babygin = 0

    while idx < len(counter):
        # 1. triplet인지 검증 : 같은 숫자가 3개 있는지
        if counter[idx] >= 3:
            counter[idx] -= 3 # 3장 이상 있는건 일단 버릴게요!라는 의미 ( 일단 triplet은 맞다는 의미 )
            is_babygin += 1

        # 2. run인지 검증 : 연속된 숫자가 3개 이상 있는지
        if idx < len (counter) -2: #인덱스가 3개씩 확인이 불가능한 8, 9는 검증을 하면 에러가 나기 때문에 빼준다.
            if counter[idx] and counter [idx + 1] and counter [idx + 2]: # 0이 아닌 숫자가 3개 연속이라면
                is_babygin += 1
                counter[idx] -= 1 # 카드를 한장씩 다 버려준다.
                counter[idx - 1] -= 1 # 카드를 안버리면 중복 연산이 있을 수 있다. 
                counter[idx - 2] -= 1 # 오류율을 낮추기 위해 ( X56789와 같이 연속된게 3개 이상일 경우 )
        idx += 1 # 다음 idx로 넘어가는 명령

    if is_babygin == 2:
        print(True)
    else:
        print(False)



