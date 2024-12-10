# We are reshaping/Resizing 1D array into 2D array (6,3)
# plz make sure while reshaping or resizing into 2D array that size of elements should be same 
# like (3,6) OR (6,3),........but not (4,6) OR (6,4)...bcoz we do not have total 24 elelments 

import numpy as np
a = np.arange(1,20) # total 20 elements (3*6)=18 or (6*3)=18 are OK !.....but not (4,6) OR (6,4)
print(a)

# a.resize(6,3)
# print(a)
# print(a.shape)

a.resize(3,6)
print(a)
print(a.shape)