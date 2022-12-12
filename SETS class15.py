#SETS
a = {1,2,3,4}
print(type(a))

a.add(5)
a.remove(2)
a.add(2)

for i in a:
    print(i)

# a = {1,2,3,4,5}
# id(1)

a ={1,2,3,4,5,}
b = {5,6,4,9}
c = (a+b)
print(c)



a = {7,8,9,4,5,6,1,2,3}
b ={1,5,9,6}
c = {a-b}
print(c)