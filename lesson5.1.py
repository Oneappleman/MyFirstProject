<<<<<<< HEAD
=======
import sys
>>>>>>> origin/master
import numpy as np
a_list = np.array([0]*10)
b_list = np.array([0]*55)
mas1 = np.zeros((3, 4))
mas2 = np.zeros((2, 4, 5))
#np.savetxt("mas.txt",a)
print("Issue1:")
#np.savetxt("mas.txt", b_list)
#np.savetxt("mas.txt", mas1)
#np.savetxt("mas.txt", mas2)
print(a_list, b_list, mas1, mas2, sep="\n")
c_list = np.array([1]*10)
d_list = np.array([1]*55)
mas3 = np.ones((3, 4))
mas4 = np.ones((2, 4, 5))
print("Issue2:")
print(c_list, d_list, mas3, mas4, sep="\n")
x1 = np.eye(5)
x_05 = np.diag([0.5, 0.5, 0.5, 0.5, 0.5])
print("Issue3:")
print(x1)
print("Issue4:")
print(x_05)
#print(x)

<<<<<<< HEAD
np.savetxt("mas1.txt", np.reshape(mas1, (3, 4)), delimiter=" ", fmt="%d")
np.savetxt("mas2.txt", np.reshape(mas2, (8, 5)), delimiter=" ", fmt="%d")
np.savetxt("mas3.txt", np.reshape(mas3, (3, 4)), delimiter=" ", fmt="%d")
np.savetxt("mas4.txt", np.reshape(mas4, (8, 5)), delimiter=" ", fmt="%d")
np.savetxt("eye1.txt", np.reshape(x1, (5, 5)), delimiter=" ", fmt="%d")
np.savetxt("eye05.txt", np.reshape(x_05, (5, 5)), delimiter=" ", fmt="%.1f")
=======
np.savetxt("mas1.txt", mas1, delimiter=",", fmt="%d")
np.savetxt("mas2.txt", mas2, delimiter=",", fmt="%d")
np.savetxt("mas3.txt", mas3, delimiter=",", fmt="%d")
np.savetxt("mas4.txt", mas4, delimiter=",", fmt="%d")
np.savetxt("eye1.txt", x1, delimiter=",", fmt="%d")
np.savetxt("eye05.txt", x_05, delimiter=",", fmt="%d")
>>>>>>> origin/master
