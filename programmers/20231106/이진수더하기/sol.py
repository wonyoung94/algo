
# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
# 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(bin1, bin2):

    int_a = int(bin1,2)
    int_b = int(bin2,2)
    bin_a = int_a + int_b

    answer = format(bin_a, 'b')
    return answer


print(solution("10", "11")) #"101"
print(solution("1001", "1111")) #"11000"

# 줄이면 이렇게 됨
# def solution(bin1, bin2):
#     answer = bin(int(bin1,2) + int(bin2,2))[2:]
#     return answer

# 2진수의 원리로 성실히 나눠준 친구
# def solution(bin1, bin2):
#     bin1, bin2 = bin1[::-1], bin2[::-1]
#     i, carry = 0, 0
#     output = ""
#     while i < len(bin1) or i < len(bin2) or carry:
#         op1 = bin1[i] if i < len(bin1) else '0'
#         op2 = bin2[i] if i < len(bin2) else '0'
#         result = int(op1) + int(op2) + carry
#         output += str(result % 2)
#         carry = result // 2
#         i += 1

#     return output[::-1]

# 난 열심히 0b를 지우려 했는데 쿨하게 집어넣고 2진수로 계산한 친구
# def solution(bin1, bin2):

#     bin1 = '0b' + str(bin1)
#     bin2 = '0b' + str(bin2)

#     return bin(int(bin1,2) + int(bin2,2))[2:]