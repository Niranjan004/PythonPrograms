N=int(input("Enter the number of rows: "))
for i in range(N-1,0,-1):
    print(" "*(N-i-1),end='')
    for j in range(i+1):
        print("* ",end='')
    print()
for i in range(N):
    print(" "*(N-i-1),end='')
    for j in range(i+1):
        print("* ",end='')
    print()
