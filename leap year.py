a=int(input('enter the year:'))
if a%4==0 and a%100!=0:
    print('given year is leap year')
else:
    print('the given year is not leap year')


output:
enter the year:1984
given year is leap year

enter the year:2025
the given year is not leap year
