import operator
l=[('pizza',100,),('burger',150),('frankie',200),('soup',120)]
print(sorted(l,key=operator.itemgetter(1)))


output:
[('pizza', 100), ('soup', 120), ('burger', 150), ('frankie', 200)]
