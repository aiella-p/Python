import numpy as np
a = np.arange(1,20) # total 20 elements (3*6)=18 or (6*3)=18 are OK !.....but not (4,6) OR (6,4)
print(a)
#a = resize(3,2,3)

a.resize(3,2,3)
print(a)
print(a.shape)