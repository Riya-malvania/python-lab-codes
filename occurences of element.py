import random
l1=[random.randint(1,20)for x in range(21)]
print(l1)
x=int(input('enter the number from above list'))
for i,a in enumerate(l1):
    if l1[i]==x:
        print('postion of the number',l1[i],'is',i) 


output:
[2, 16, 18, 20, 3, 17, 20, 16, 15, 6, 4, 4, 5, 7, 10, 19, 17, 16, 8, 8, 5]
enter the number from above list16
postion of the number 16 is 1
postion of the number 16 is 7
postion of the number 16 is 17


