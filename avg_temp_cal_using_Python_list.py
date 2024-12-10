# Calculate Average Temp using Python Lists
# note we can calculate using Array Data structures....as well to get the same results


numDays = int(input("How many's days temp req ?: "))

total = 0 
temp = [] # empty list we are creating here ....for later use ....
for i in range(numDays): # start = 1, stop = numDays + 1 (bcoz stops always n -1)
    nextDay = int(input("Day" + str(i+1) + "'s high temp in Deg C: "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total/numDays,2)    
print("\nAverage Temp in Deg C = " + str(avg))

# To find No of Days are greater than this Average temp, now we have ave temp stored in temp = [] list,
# and we are going to loop through this list temp = [] and finding out temp that are 
# above average temp as below steps.....

 # we are setting a variable name above = 0 initially as 0 number of days 
#as greater than avg temp
above = 0
for i in temp:
   if i > avg:
    above += 1 # OR above = above + 1

print(str(above) + " Day(s) above average")    

