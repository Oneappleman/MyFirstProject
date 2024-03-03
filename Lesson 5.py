import matplotlib.pyplot as mpl
from numpy.random import shuffle
import memory_profiler
x = [i for i in range(1, 5)]
#b_list = [i for i in range(50, 100)]
shuffle(x)
print(x)
#shuffle(b_list)
#a = np.array([a_list, b_list])
#print(a, type(a))
#print(a[1][3])
mpl.plot(x)
mpl.show()
