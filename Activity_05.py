numbers=input("Enter 5 numbers:")
list=numbers.split()
sum = 0
for i in list:
    sum=sum+float(i)
print("Sum of all the numbers is = {}".format(sum))
