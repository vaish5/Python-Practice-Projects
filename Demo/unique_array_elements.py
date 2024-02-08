arr = input().split()
# flag = False
# unique_count = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] != arr[j]:
#             flag = True
#     if flag:
#         unique_count += 1
# print(unique_count)
count = 0
for ele in arr:
    if arr.count(ele) == 1:
        count += 1
print(count)
