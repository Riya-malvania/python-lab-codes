import random
l1=[random.randint(-20,20)for x in range(51)]
print('list of random integers range from 1 to 30')
print(l1)
l2=[]
l3=[]
for i in l1:
    if i<0:
        l2.append(i)
    if i>0:
        l3.append(i)
print('list of positive values:')
print(l3)
print('list of negative values:')
print(l2)

output:
list of random integers range from 1 to 30
[9, 14, 2, -5, -8, -12, -4, -15, -16, -16, -20, 12, 5, -19, -4, 19, -11, -1, 19, -8, 1, 2, -20, 18, -15, -3, -17, -6, -15, -8, 14, -12, 11, 8, 13, 4, 9, 14, 9, -12, -19, -6, -2, 4, 18, -7, -5, 19, -5, 15, -9]
list of positive values:
[9, 14, 2, 12, 5, 19, 19, 1, 2, 18, 14, 11, 8, 13, 4, 9, 14, 9, 4, 18, 19, 15]
list of negative values:
[-5, -8, -12, -4, -15, -16, -16, -20, -19, -4, -11, -1, -8, -20, -15, -3, -17, -6, -15, -8, -12, -12, -19, -6, -2, -7, -5, -5, -9]
