
# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.


# 정렬 해서 제일 큰 수 두개(양수가 곱해질 경우)랑 
# 제일 작은 수 두개(음수 두개가 곱해질 경우)랑 곱한 값을 비교해서 더 큰 값 return

def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])



print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))
