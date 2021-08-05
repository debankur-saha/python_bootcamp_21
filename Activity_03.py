string1=input("Enter 1st word: ")
string2=input("Enter 2nd word: ")
output=(string1,string2)*5
print(string1,string2)
print(*output,sep='')
