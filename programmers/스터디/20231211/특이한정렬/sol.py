
# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 
# 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 
# numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numlist, n):
    # numlist를 sort 후 
    # 딕셔너리 형태로 각 요소와의 차이를 적어서 절대값 처리
    # zip 함수를 이용해 튜플로 각각 묶어서 반환 : 실패
    # 튜플[인덱스]에 맞는 원소를 answer에 append : 실패
    # lambda 함수로 튜플 생성 후 key값 반환
    return sorted(numlist, key = lambda x: (abs(x - n), -x))

# 다른사람의 추가 설명
# key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다. 
# 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다. 
# 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열되는 것 같다(인덱스가 작은 것이).
print(solution([1, 2, 3, 4, 5, 6], 4)) #[4, 5, 3, 6, 2, 1]
print(solution([10000,20,36,47,40,6,10,7000], 30)) #[36, 40, 20, 47, 10, 6, 7000, 10000]

# zip 함수 쓴사람 : 파이썬튜터 보는거 추천(안보면 이해 어려울 수 있음)
# def solution(numlist, n):
#     numlist2=numlist.copy()
#     # numlist2의 각 요소에서 n을 뺀 후 절대값 처리
#     for i in range(len(numlist2)):
#         if numlist2[i]-n>=0:
#             numlist2[i]=numlist2[i]-n
#         else:
#             numlist2[i]=-(numlist2[i]-n)
#     # 원본 및 수정된 값을 포함하는 튜플 목록 작성
#     ans=[i for i in zip(numlist,numlist2)]
#     # 두 가지 기준으로 목록 정렬
#     ans=sorted(sorted(ans,key=lambda x:-x[0]),key=lambda x:x[1])
#     print(ans)
#     return [i[0] for i in ans]

# collection 함수 import 해서 사용
# from collections import defaultdict

# def solution(numlist, n):
#     diff_dict = defaultdict(list)

#     for num in numlist:
#         diff_dict[abs(num-n)].append(num)

#     answer = []
#     for diff, nums in sorted(diff_dict.items(), key=lambda v: v[0]):
#         nums = sorted(nums)
#         while nums:
#             answer.append(nums.pop(-1))

#     return answer
