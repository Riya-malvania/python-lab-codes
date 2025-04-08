f=open('riya.txt','r')
x=f.read()
y=x.split()
print(y)
for i in y:
    c=y.count('riya')
print('no of occurences of riya :',c)
    


output:
['riya', 'is', 'good', 'girl', 'riya', 'study', 'in', 'pdeu', 'riya', 'likes', 'to', 'watch', 'movies', 'riya', 'is', 'hardworking', 'girl', 'riya', 'can', 'achieve', 'anything']
no of occurences of riya : 5
