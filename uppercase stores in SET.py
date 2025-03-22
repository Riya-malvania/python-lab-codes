l=['riya','shikha','jeet','aarav','vansh']
print('list of words with lower case:',l)
l1=[]
for i in l:
    l1.append(i.upper())
s=set(l1)
print('set with uppercase elements of list',s)


output:
list of words with lower case: ['riya', 'shikha', 'jeet', 'aarav', 'vansh']
set with uppercase elements of list {'SHIKHA', 'VANSH', 'JEET', 'RIYA', 'AARAV'}
