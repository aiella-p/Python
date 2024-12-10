#In this case, else block will not be executed.

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i = i + 1
else:
    print("Done. while loop executed normally")