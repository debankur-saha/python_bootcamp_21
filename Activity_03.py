string1=input("Enter 1st word: ")
string2=input("Enter 2nd word: ")
output1=(string1,string2)
output2=(string1,string2)*5
print(*output1,sep='')
print(*output2,sep='')
