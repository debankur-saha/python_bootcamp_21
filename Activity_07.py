numbers=input("Enter 2 numbers:")
list=numbers.split()
sum = 0
for i in list:
    sum=sum+float(i)
print(*list[0], "+", *list[1], "=", sum)
