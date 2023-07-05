def switch(x,y):
    x,y=y,x
    print("inside switch:",end='')
    print("x=",x,"y=",y)
x=5
y=7
switch(x,y)
print("the old x,y are",x,y)