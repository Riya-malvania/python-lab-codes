l=[('r'),('t',7),('b'),(1.3),(1,3,5),(),()]
l1=[]
print('list of tuples with empty tuples',l)
for tup in l:
    if tup:
        l1.append(tup)
print('list of tuples after removing empty tuples',l1)


output:
list of tuples with empty tuples ['r', ('t', 7), 'b', 1.3, (1, 3, 5), (), ()]
list of tuples after removing empty tuples ['r', ('t', 7), 'b', 1.3, (1, 3, 5)]
