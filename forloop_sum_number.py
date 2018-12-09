#sum 1234 ------>1+2+3+4

total=0
num = input("Enter number ")
for i in range(0,len(num)):
    total += int(num[i])
print(total)    