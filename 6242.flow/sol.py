import sys
sys.stdin = open('input.txt')

# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A': 0,
    'B': 0,
    'O': 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] +=1

print(blood_dict)

#############  Key 값이 한정적이지 않을 경우 #############

location_list = ['서울', '부산', '부산', '서울', '대전', '광주', '제주']

location_dict = {}

for location in location_list:

    if location in location_dict.keys():
        location_dict[location] += 1 
        # Key값이 있는 경우 1 카운팅
    else:
        location_dict[location] = 1 
        # Key는 location, value는 1로 입력

print(location_dict)