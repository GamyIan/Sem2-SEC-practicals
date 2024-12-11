n=int(input("Enter number of tables: "))
l=[]
for i in range(n):
    m=int(input(f"Enter number of which table you want: "))
    table=[]
    for j in range(1,11):
        table.append(m*j)
    l.append(table)

print(l)