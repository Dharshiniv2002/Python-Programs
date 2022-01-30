list=[4,1,5,2,3]
count=0
search=int(input("enter search number"))
for i in range(0,len(1ist)):
    if search==list[i]:
    print(str(search)+"found at position"+str(i+1))
    count=1
    break
if count==0:
    print("Element not found")
            
