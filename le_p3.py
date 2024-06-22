x=int(input("enter the number of rows: "))
n=65
for i in range(1,x+1):
    for j in range(1,i+1):
        print(chr(n),end="")
        n+=1
    print()