# Use list slicing. We can access a list of elements from a list using list slicing.

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[2::2]:
    print(i, end=" ")