import matplotlib.pyplot as plt 
import matplotlib.dates as mdates


x = [1,2,3,4,5,6,7,8,9]  #values of x


a =  raw_input('Please enter the list of time series values: ') #enter in list format i.e [112, 2233, 22333, 3333]


times =  int(raw_input('How many times will you like to perform expo smoothing?: '))

global alpha

def get_alpha(): #smoothing value here
	global alpha
	alpha = float(raw_input('Enter the smoothing constant btw 0 and 1: '))
	return alpha

b = [a[0], a[0]]  #initialize a  list of forecast for time period t + 1 
#since forecast forecast for tiime period T1 = the first Time series,


def expo_smoothing():

	get_alpha()
	#creating an index to use in the while loop for creating the list of forecast for time period t+1
	n = 2
	#here is the loop that will create the list
	while n < len(a):

		global alpha
		forecast =  ( alpha * a[n-1] ) + ((1- alpha)*b[n-1])

		
		b.append(forecast)

		n += 1

	#so lets get to the function that allows us perform exponential smoothing over a given set of smoothing values

	plt.plot(x, y)
	plt.plot(x, y2)
	plt.ylim([0, 3000])
	plt.show()
	


while times > 0:
	expo_smoothing()
	times -= 1


