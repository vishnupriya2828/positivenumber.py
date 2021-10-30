li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)

print("Positive numbers in",li,"are: ")
  
pos_num = list(filter(lambda x: (x>=0),li))  
print(pos_num)
