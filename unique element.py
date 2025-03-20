l1=[1,2,5,6,13,45,56]
l2=[1,2,3,4,5,6,8,9,5]
l3=[]
print('l1=',l1)
print('l2=',l2)
for i in l1:
    if i not in l2:
        l3.append(i)
print('numbers present in l1 only')
print(l3)

output:
l1= [1, 2, 5, 6, 13, 45, 56]
l2= [1, 2, 3, 4, 5, 6, 8, 9, 5]
numbers present in l1 only
[13, 45, 56]
