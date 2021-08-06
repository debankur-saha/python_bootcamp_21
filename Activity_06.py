numbers=input("Enter 5 numbers:")
list=numbers.split()
sliced_list= list[0:3]
print("sliced list=[", *sliced_list, "]")
list[0]="0"
sliced_list[0]="0"
print("replaced list-1=[", *list, "]")
print("replaced list-2=[", *sliced_list, "]")
