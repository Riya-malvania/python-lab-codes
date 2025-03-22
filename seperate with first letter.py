s={'aarav','brookie','ansh','bailey'}
s1=set()
s2=set()
for i in s:
    if i.startswith('a'):
        s1.add(i)
    else:
        s2.add(i)
print('set with a names',s1)
print('set with b names',s2)


output:
set with a names {'ansh', 'aarav'}
set with b names {'bailey', 'brookie'}
