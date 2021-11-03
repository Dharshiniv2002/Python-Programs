def search(list1,key):
    for i in range(len(list1)):
        if key ==list1[i]:
            print("Element found at index: ",i)
        
        else:
            print("Element is not found: ",i)
            break
list1 = [5,7,25,100,26,55,77,9,2,1]
key = int(input("Enter the key element: "))
search(list1,key)
