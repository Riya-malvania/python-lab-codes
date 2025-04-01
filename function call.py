def fun():
    print('function called')
def disp():
    print('disp called')

def msg():
    print('msg called')
function=[fun,disp,msg]
for f in function:
    f()

output:
function called
disp called
msg called
