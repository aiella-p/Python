# Note:

# In the first iteration of the outer loop, the inner loop executes five times.
# In the second iteration of the outer loop, the inner loop executes four times.
# In the last iteration of the outer loop, the inner loop will execute only once.

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()