l1=['riya','aaaryaman','jaydeeeep','yesha']
x=len(l1)
a=filter(lambda i:len(i)>8,l1)
print(list(a))


output:
['aaaryaman', 'jaydeeeep']
