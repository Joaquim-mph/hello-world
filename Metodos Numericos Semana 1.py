import math
import matplotlib.pyplot as plt

e = 1 
e_vs_n = [e]

k_factorial = 1
N_max = 18

for k in range(1, N_max):
    k_factorial *= k
    e += 1/k_factorial
    e_vs_n.append(e)

#for i in range(N_max):
#    print (i, "->", e_vs_n[i])

plt.figure(1, figsize=(7,3))
plt.plot(range(N_max), e_vs_n)
plt.axhline(math.e, color="0.5")

plt.ylim(0,3)
plt.xlabel("N",fontsize=20)
plt.ylabel("$e_n$",fontsize=20);
plt.show()