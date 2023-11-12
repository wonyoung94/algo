
# 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 
# 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
# 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, 
# k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.

# 환형 큐 문제 같은데...어케 접근 해야 하누..

from collections import deque

def solution(numbers, k):
    n = len(numbers) 
    answer = [] 

    # 일단 deque를 써서 원형 큐를 만들어줍니다....
    circular_queue = deque(numbers)
    for i in range(k):
        # 두칸씩 미뤄줍시다... ( . . . 1 2 3 4 1 2 3 4 1 2 3 4 . . . )
        circular_queue.rotate(-2)
        answer.append(circular_queue[0]) # 3 1 3 1 3 1 3 1

    return answer[k-2]

print(solution([1, 2, 3, 4], 2)) #[3, 1]
print(solution([1, 2, 3, 4, 5, 6], 5))  # [3, 5, 1, 3, 5]
print(solution([1, 2, 3], 3))  # [3, 2, 1]


# 나 뭐함? 자괴감 지린다...이해하고 싶지도 않아졌어...ㅠㅠ
# def solution(numbers, k):
#     return numbers[2 * (k - 1) % len(numbers)]

# 내껄 또 줄였네...ㅠㅠ
# from collections import deque
# def solution(numbers, k):
#     array = deque(numbers)

#     array.rotate(-(k-1)*2)

#     return array[0]

# 민정이 답
# import math

# def solution(numbers,k):
#     n= int(math.ceil((2*k)/len(numbers)))
#     answer = []

#     for _ in range(n):    
#         for i in numbers:
#             answer.append(i)  # [1 2 3 4 5 6 1 2 3 4 5 6]  
    
#     return answer[k*2-2]    


# print(solution([1, 2, 3, 4, 5, 6],5))


# 3 : 인덱스 0, 1번쨰로 받은 사람, 2번째로 던질 사람
# 1 : 인덱스 1, 2번쨰로 받은 사람, 3번쨰로 던질 사람
# 3 : 인덱스 2, 3번쨰로 받은 사람, 4번쨰로 던질 사람
# 1 : 인덱스 3, 4번쨰로 받은 사람, 5번쨰로 던질 사람
# 3 : 인덱스 4, 5번쨰로 받은 사람, 6번쨰로 던질 사람
# 1 : 인덱스 5, 6번쨰로 받은 사람, 7번쨰로 던질 사람
# 3 : 인덱스 6, 7번쨰로 받은 사람, 8번쨰로 던질 사람
# 1 : 인덱스 7, 8번쨰로 받은 사람, 9번쨰로 던질 사람
# 3 : 인덱스 k-2 , k-1 번쨰로 받은 사람, k번쨰로 던질 사람