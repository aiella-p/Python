# Calculate Average Temp

numDays = int(input("How many's days temp req ?: "))

total = 0 
for i in range(1, numDays + 1): # start = 1, stop = numDays + 1 (bcoz stops always n -1)
    nextDay = int(input("Day" + str(i) + "'s high temp in Deg C: "))
    total += nextDay

avg = round(total/numDays, 2)    
print("\nAverage Temp in Deg C = " + str(avg))

