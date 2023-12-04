
# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

    # 각 평균을 구한다
    # 정렬된 기준을 구한다
    # 기준의 인덱스값을 answer에 append 한다.

def solution(scores):
    answer = []
    
    for i, score in enumerate(scores, start=1): #각 학생에게 1번부터 번호표 부착
        avg_score = sum(score) / len(score) #각 학생의 평균 계산(len(score)대신 2를 넣어도 됨.)
        
        rv_student = 0 # rv = Reference value(등수)

        for student in scores:
            rv_score = sum(student) / len(student) # 전체 평균을 구해서 rv_score 작성

            if rv_score > avg_score: # 학생 score가 평균보다 크면
                rv_student += 1 # 등수를 하나 올려준다.(1등보다2등이 낮은 거임, 숫자가 올라갈수록 낮은 등수)

        answer.append(rv_student + 1)

    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))  # [1, 2, 4, 3]
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))  # [4, 4, 6, 2, 2, 1, 7]

# index 함수 사용
# def solution(score):
#     a = sorted([sum(i) for i in score], reverse = True)
#     return [a.index(sum(i))+1 for i in score]

