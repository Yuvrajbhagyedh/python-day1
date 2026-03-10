import numpy as np
import time
li=[1,2,3,43,5,3]

b=np.array(li)
start=time.time()
print(b*2)
print(time.time()-start)
