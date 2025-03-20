import random
l1=[random.randint(1,30)for x in range(51)]
print('list of random integers range from 1 to 30')
print(l1)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print('list after removing duplicate values')
print(l2)

output:
list of random integers range from 1 to 30
[7, 6, 21, 2, 8, 18, 30, 25, 7, 23, 11, 23, 14, 13, 19, 6, 8, 10, 10, 26, 16, 1, 28, 2, 12, 22, 3, 27, 19, 12, 4, 26, 20, 1, 11, 18, 30, 10, 17, 24, 24, 6, 21, 25, 17, 12, 24, 30, 28, 28, 4]
list after removing duplicate values
[7, 6, 21, 2, 8, 18, 30, 25, 23, 11, 14, 13, 19, 10, 26, 16, 1, 28, 12, 22, 3, 27, 4, 20, 17, 24]
