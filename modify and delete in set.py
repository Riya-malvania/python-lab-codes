s=set()
for i in range(5):
    x=input('enter the name:')
    s.add(x)
print(s)
x=input('enter the name to delete:')
s.remove(x)
print(s)
z=int(input('enter the index num to modify:'))
y=input('enter the name to modify:')
l=list(s)
l[z]=y
s1=set(l)
print(s1)


output:
enter the name:q
enter the name:w
enter the name:e
enter the name:r
enter the name:t
{'q', 'w', 't', 'r', 'e'}
enter the name to delete:q
{'w', 't', 'r', 'e'}
enter the index num to modify:2
enter the name to modify:riya
{'riya', 't', 'e', 'w'}
