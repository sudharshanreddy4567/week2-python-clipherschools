#tuples class 14
a = (1,2,3,4,5)
print(type(a))

def func(*args):
    print(type(args))
func(1,2,3,4,5)

a= 5
b= 9
a,b = b,a
c = a,b
type(c)

def sum_diff(a,b):
    s = a+b
    d = a-b

    return s,d

a = [1,2,3,4,5]
list(range(5))
tuple(range(5))

a = [1,2,3,4,5]
a.append(5) 

a = {"name" : "asif",
     "company : shutl",
     "college :  lpu"
}
key = "marks"
print(a.get(key, "key doesnt exist"))