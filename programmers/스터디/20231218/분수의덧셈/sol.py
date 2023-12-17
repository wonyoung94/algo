
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 
# 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

import math

def solution(numer1, denom1, numer2, denom2):
    result_num = (denom2 * numer1) + (denom1 * numer2)
    result_den = denom1 * denom2
    math.gcd(result_den, result_num)
    return [int(result_num/(math.gcd(result_den, result_num))), int(result_den/(math.gcd(result_den, result_num)))]


print(solution(1, 2, 3, 4)) #[5, 4]
print(solution(9, 2, 1, 3)) #[29, 6]


# 다 비슷하게 해서 이건 PASS