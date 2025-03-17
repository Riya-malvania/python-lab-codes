p=int(input('enter the marks in physics;'))
b=int(input('enter the marks in biology;'))
c=int(input('enter the marks in chemistry;'))
avg=(p+b+c)/3
print('the average marks is:',avg)
print('the grades obtained:')
if avg>=80:
    print('distinction')
elif avg>=60:
    print('first division')
elif avg>=45:
    print('second division')
elif avg>=40:
    print('pass')
else:
    print('promotion not granted')

output:
enter the marks in physics;80
enter the marks in biology;90
enter the marks in chemistry;95
the average marks is: 88.33333333333333
the grades obtained:
distinction
