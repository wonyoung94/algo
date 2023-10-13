my_list = [1, 5, 7, 8, 8, 5, 1, 4, 2, 3, 4 ]

counter = [0 for i in range(10)]

for num in my_list:
    counter[num] += 1

# print(counter)

result = []

for value, count in enumerate(counter):
    # print(value, count)
    for i in range(count):
        result.append(value)

print(result)