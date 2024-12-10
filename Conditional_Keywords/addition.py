def addition():
    x = int(input("Please enter the first number:"))
    y = int(input("Please enter the second number:"))
    z = x+y
    #print("The sum of " + str(x) + " and " + str(y) + " gives " + str(z))
    print("The sum of {0} and {1} gives {2}".format(x, y, z))
addition()    