import random
s={random.randint(15,45)for i in range(11)}
print('set of radom numbers between 15 to 45',s)
y=0
for x in s:
    if x<30:
        y=y+1
print('no less than 30:',y)


output:
set of radom numbers between 15 to 45 {32, 37, 45, 17, 20, 22, 23, 25, 28, 31}
no less than 30: 6
