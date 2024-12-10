numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break # If break used it will stop further
    elif item > 150:
        continue # if continue keyword use, 
    # it will skip that particular element(150) from the list and continues further
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)
