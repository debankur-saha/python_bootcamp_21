string1=input("Enter 1st word: ")
string2=input("Enter 2nd word: ")
output1=(string1+string2)
output2=(string1+string2)*5
output3=(string1, " ", string2, "\n")*5
print(output1)
print(output2)
print(*output3, sep='')
