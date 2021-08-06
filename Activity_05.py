numbers=(input("Enter 5 numbers:"))
list=numbers.split()
sum = 0
for i in list:
    sum=sum+float(i)
print("The sum of the 5 numbers is {}".format(sum))
