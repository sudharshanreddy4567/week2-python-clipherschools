# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# func(1,2,3)

# print(1,2,3,4,5,sep = ",")

def func(a,b):
    print(a,b)
func(1,2)

def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,d=8)

a = lambda a,b: a+b
a(1,2)