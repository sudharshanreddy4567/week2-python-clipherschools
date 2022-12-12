a = []
for i in range (5):
    a.append(i)

print(a)

[i for i in range(6) ]

list(map(lambda x: x**2 ,range(5)))

n = 5
[[max(i+1 , j+1 , n-1 , n-j) for j in range(n)] for i in range(n)]

a = [i for i in range(6)]
print(type(a))