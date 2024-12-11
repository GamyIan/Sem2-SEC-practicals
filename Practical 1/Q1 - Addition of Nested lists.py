#Write a program to perform addition of 2 nested lists

l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[10,11,12],[13,14,15],[16,17,18]]
l3=[]

m=len(l1)
n=len(l1[0])

for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(l1[i][j]+l2[i][j])
    l3.append(temp)

print(l3)
