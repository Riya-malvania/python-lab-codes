n=int(input('enter the no of element in list'))
l1=[]
l2=[]
for i in range(n):
    t=int(input('enter the fahrenheit:'))
    l1.append(t)
print(l1)
for j in l1:
    c=(j-32)*5/9
    l2.append(c)
print(l2)


output:
enter the no of element in list3
enter the fahrenheit:450
enter the fahrenheit:32
enter the fahrenheit:350
[450, 32, 350]
[232.22222222222223, 0.0, 176.66666666666666]
