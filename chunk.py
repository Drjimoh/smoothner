import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

x = [1,2,3,4,5,6,7,8,9]

a = [1195, 1349, 2265, 2304, 2732, 2130, 1971, 1312, 1268] 

n = 2

b = [1195, 1195]

alpha = 0.01
 




while n < len(a):
	forecast =  ( alpha * a[n-1] ) + ((1- alpha)*b[n-1])

	
	b.append(forecast)

	n += 1


print b

plt.plot(x, b)
plt.plot(x, a)
plt.ylim([0, 3000])
plt.grid(True)
plt.show()






