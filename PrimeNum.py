num = int(input("Enter the number : "))

prime = False

for i in range(2,num):
    if num % i == 0:
        #print("Not Prime")
        prime = False
        break
    else:
        prime = True
        #print("Prime Number")

if prime:
    print("Prime Number")

else:
    print("Not Prime")
