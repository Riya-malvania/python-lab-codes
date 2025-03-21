l=[('jeet',),('vansh',),('aarav',),'riya','shikha','urvi']
print(l)
x=0
y=0
for i in l:
    if isinstance(i,tuple):
        x=x+1
    else:
        y=y+1
print('no of boys:',x)
print('no of girls:',y)


output:
[('jeet',), ('vansh',), ('aarav',), 'riya', 'shikha', 'urvi']
no of boys: 3
no of girls: 3
