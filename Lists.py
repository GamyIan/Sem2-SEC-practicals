def take_list(n):
    l=[]
    for i in range(n):
        l.append(int(input(f"Enter element {i+1}: ")))
    return l


n=int(input("Enter number of elements: "))
l1,l2,l3=[],[],[]

print("Enter elements for l1")
l1=take_list(n)

print("Enter elements for l2")
l2=take_list(n)

for i in range(n):
    l3.append(l1[i]**l2[i])
    
print(f"L3 = {l3}")
