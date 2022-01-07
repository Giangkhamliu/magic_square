n=int(input("Enter the number of rows and columns:"))
i=0
a=[]
while i<n:
    j=0
    b=[]
    while j<n:
        num=int(input("Enter the desired numbers:"))
        b.append(num)
        j+=1
    a.append(b)
    print()
    i+=1
print(a)
print()
t=0
print("Magic_Square=")
while t<len(a):
    q=0
    while q<len(a[t]):
        print(a[t][q],end=" ")
        q=q+1
    print()
    t=t+1
print()
i=0
while i<len(a):
    row=0
    j=0
    while j<len(a):
        row=row+a[i][j]
        j+=1
    i+=1
    print("Row=",row)
print()

j=0
while j<len(a):
    col=0
    i=0
    while i<len(a):
           col=col+a[i][j]
           i+=1
    j+=1
    print("col=",col)
print()

i=0
j=0
f=(len(a)-1)
d1=0
d2=0
while i<len(a):
    d1=d1+a[i][j]
    d2=d2+a[i][f]
    i+=1
    j+=1
    f-=1
print("Diagonal=",d1)
print("Diagonal",d2)
if row==col==d1==d2:
    print("yes,it is magic square")
else:
    print("No,it is not magic square")

    
