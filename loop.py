def test(n):
    y=1
    for i in range(1,n):
        if y%2==0:
            print(y)
        y=y+1

n=int(input("Enter no:"))
test(n)    
