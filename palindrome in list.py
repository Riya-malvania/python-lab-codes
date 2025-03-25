l=['madam','python','malayalam','12321']
for x in l:
    if str(x)==str(x[::-1]):
        print(x)


output:
madam
malayalam
12321
