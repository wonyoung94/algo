
# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 난 니가 싫어..ㅠ
# 문자열 numbers가 매개변수로 주어질 때, 
# numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

def solution(numbers):
    answer = ""
    my_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven':7,
        'eight':8,
        'nine':9,
        'zero':0,
        }
    
    i = 0 #자릿수 체크용 
    while i < len(numbers): # i가 numbers 를 다 돌때까지
        for word in my_dict.keys(): # my_dict에 있는 keys를 다 확인해라
            if numbers[i:i + len(word)] == word: # i:i + len(word) => (ex .one: 3) 가 one과 같다면 : 안할경우 1112223333344...가 됨
                answer += str(my_dict[word]) # my_dict의 word를 str화 해서 answer에 넣어라
                i += len(word) # i는 len(word)만큼 더 이동한다(ex .one: 3) : 효율성을 위해
                break

    return int(answer) # 에이쒸ㅜㅠ 원하는건 또 int 형이라 또 변환함 ㅋㅋㅋ

print(solution("onetwothreefourfivesixseveneightnine")) # 123456789
print(solution("onefourzerosixseven")) # 14067

# 내 코드 효율적으로 줄인 경우(대충 머리가 나쁘면 돌아간다는 뜻)
# def solution(numbers):
#     r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
#          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
#     for k in r.keys():
#         numbers = numbers.replace(k, r[k])
#     return int(numbers)

# replace 함수 사용했을 경우
# def solution(numbers):
#     dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     i=0
#     for word in dic:
#         numbers = numbers.replace(word, str(i))
#         i+=1
#     return int(numbers)

# enumerate와 replace 사용한 함수
# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
#         numbers = numbers.replace(eng, str(num))
#     return int(numbers)

# 한솔이 답
# def solution(numbers):
#     # 인덱스 만들기(단어가 의미하는 숫자 = 인덱스)
#     eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     for char in eng:
#         if char in numbers:
#             # 반복문으로 eng 내부 숫자가 포함되는지 확인하고 변환
#            numbers = numbers.replace(char, str(eng.index(char)), numbers.count(char))
        
#     return int(''.join(numbers))