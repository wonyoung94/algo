
# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
# 정수 배열 emergency가 매개변수로 주어질 때 
# 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(emergency):

    # 머쓱이 의사야?
    # 누구 맘대로 진료 순서를 정해 임마....
    # 요즘 세상에 이러면 큰일나...

    # 정렬한 변수의 인덱스값+1을 매칭하믄 대겠네!
    answer = []
    s_emr = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(s_emr.index(i)+1)

    return answer


print(solution([3, 76, 24])) #[3, 1, 2]
print(solution([1, 2, 3, 4, 5, 6, 7])) #[7, 6, 5, 4, 3, 2, 1]
print(solution([30, 10, 23, 6, 100])) #[2, 4, 3, 5, 1]


# 코드만 짧지 for문 하위에서 나오는 sorted 호출은 많은 자원이 사용될 수 있다.
# def solution(emergency):
#     return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

# 딕셔너리를 사용해서 만든 코드
# 딕셔너리를 사용할 경우, 인덱스 사용시 O(N**2)로 효율이 좋다고 합니다.
# 이 코드는 꼭 파이썬 튜터로 확인하기!!! 해보면 직관적으로 확인 가능
# def solution(emergency):
#     dict1={}
#     list1=sorted(emergency,reverse=True)
#     for i,x in enumerate(list1,start=1):
#         dict1[x]=i
#     answer=[dict1[x] for x in emergency]
#     return answer