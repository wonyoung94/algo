# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     P, Pa, Pb = map(int, input().split())
#     A, B, get = 0, 0, 0 
#     l, r = 1, P

#     while get < 2:
#         if Pa != l and Pa !=  r:
#             A += 1
#             B += 1
#             C = (l + r) // 2
#             if Pa < C:
#                 r = C
#             else:
#                 l = C
#             if Pa == C:
#                 get += 1
#         else:
#             get += 1

#     print(f'#{tc} A' if A < B else f'#{tc} B' if A > B else f'#{tc} 0')

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    # P : 책의 장수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지
    P, A, B = list(map(int, input().split()))

    left = 1
    right = P
    A_count = 0 

    while True:
        center = int((left+right)/2)

        # A의 목적페이지가 가운데보다 왼쪽에 있는경우
        # 오른쪽 데이터를 지우기
        if A < center:
            right = center
        # A의 목적페이지가 가운데보다 오른쪽에 있는경우
        # 왼쪽 데이터를 지우기
        elif center < A:
            left = center
        # A의 목적페이지에 도달한 경우
        else:
            break

        A_count += 1

    left = 1
    right = P
    B_count = 0

    while True:
        center = int((left+right)/2)

        if B < center:
            right = center
        elif center < B:
            left = center
        else:
            break

        B_count += 1

    print(A_count, B_count)



# 도현님 코드
# for tc in range(1, T+1):
#     P, Pa, Pb = map(int, input().split())
#     A, B = 0, 0
#     get = 0
#     l = 1
#     r = P

#     while get == 0:
#         if Pa != l and Pa != r:
#             A += 1
#             if Pa < int((l+r)/2):
#                 r = int((l+r)/2)
#             elif Pa > int((l+r)/2):
#                 l = int((l+r)/2)
#             else:
#                 get += 1
#             # print(l, r, A, Pa, get)
#         else:
#             get += 1

#     get = 0
#     l = 1
#     r = P
#     while get == 0:
#         if Pb != l and Pb != r:
#             B += 1
#             if Pb < int((l+r)/2):
#                 r = int((l+r)/2)
#             elif Pb > int((l+r)/2):
#                 l = int((l+r)/2)
#             else:
#                 get += 1
#             # print(l, r, A, Pa, get)
#         else:
#             get += 1
#     print(f'#{tc} A') if A < B else (print(f'#{tc} B') if A > B else print(f'#{tc} 0'))

# 가영님 코드
#  P, A, B = map(int, input().split())
#     a_count = 0
#     b_count = 0
#     l = 1
#     r = P

#     while True:
#         a_count += 1
#         C = int((l+r)/2)

#         # A의 경우
#         if C == A:
#             break
#         elif C <= A:
#             l = C
#             r = P
#         else:
#             r = C

#     while True:
#         b_count += 1
#         C = int((l+r)/2)

#         # B의 경우
#         if C == B:
#             break
#         elif C <= B:
#             l = C
#             r = P
#         else:
#             r = C
    
#     if a_count > b_count:
#         print(f'#{tc}', 'A')
#     elif b_count > a_count:
#         print(f'#{tc}', 'B')
#     else:
#         print(f'#{tc}', '0')

