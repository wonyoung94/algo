my_list = [1, 5, 7, 8, 8, 5, 1, 4, 2, 3, 4 ]

for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        # print(left, right)
        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j] # 리스트에서 위치 순서 바꾸는 방법