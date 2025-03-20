l1=[]
l2=[]
for i in range(5):
    x=int(input('enter any  odd number:'))
    l1.append(x)
    
for j in range(4):
    y=int(input('enter the even number'))
    l2.append(y)
    
print('l1=',l1)
print('l2=',l2)
print('by replacing third element of l1 with l2')
l1[2]=l2
print(l1)

output:
enter any  odd number:7
enter any  odd number:5
enter any  odd number:3
enter any  odd number:1
enter any  odd number:9
enter the even number2
enter the even number4
enter the even number6
enter the even number8
l1= [7, 5, 3, 1, 9]
l2= [2, 4, 6, 8]
by replacing third element of l1 with l2
[7, 5, [2, 4, 6, 8], 1, 9]
