r=[]

m=int(input("Enter number of rows: "))
for i in range(m):
    c=[]
    n=int(input(f"Enter number of columns for row {i+1}: "))
    for j in range(n):
        inp=input(f"Enter element [{i+1}][{j+1}]: ")
        c.append(inp)
    r.append(c)
    
print(r)
    