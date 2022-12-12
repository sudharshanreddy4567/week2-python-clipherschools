a=[1,2,3,4,5]
print(a)
c=[2,4,6,8]
c[1]=1000
print(c)
#python expressions:
print(len(c))
print(a+c)
print(a*2)
print(c*3)
m=[0,9,8,7,6,5,4,3]
for x in m:
    print(x)
k=[2,3,4,5,6,7]
print(k[-2])
print(len(k)-1)
v=[1,4,6]
print(v.append(v))
print(v.insert(1,100))
print(v.pop())
print(v)
z=["toy","bunny","screen","exam","bunny"]
print(z.remove("bunny"))
print(z)
p=[2,4,6,8,0]
print(p.sort())
print(p)
print(reversed(p))
for x in reversed(p):
    print(x)
f=[2,4,16,36]
for x in map(lambda x: x**2,f):
    print(x)
