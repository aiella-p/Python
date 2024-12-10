#check stock of phones in store

stock = 5
x = int(input("How many phones you want: "))
i = 1 # Here we have to take 1 bcoz, customer will buy minimum 1 phone !!!
#we should not initialise this variable as 0 !!! 
while i <= x:
    if i >stock:
        print("out of stock")
        break
    print("phones")
    i+=1
print("bye")    