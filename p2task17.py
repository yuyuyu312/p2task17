a = [1  ,4 , 5 , 6, 7 , 8 ,9, 10]
b = []
for i in range(a[0], a[-1]+1):
    if i not in a:
        b.append(i)
print(b)
