import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt

# prints formatted price
def formatPrice(n):
	return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

# returns the vector containing stock data from a fixed file
def getStockDataVec(key):
	vec = []
	lines = open("data/" + key + ".csv", "r").read().splitlines()

	for line in lines[1:]:
		vec.append(float(line.split(",")[4]))

	return vec

# returns the sigmoid
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

# returns an an n-day state representation ending at time t
def getState(data, t, n):
	d = t - n + 1
	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0
	res = []
	for i in range(n - 1):
		res.append(sigmoid(block[i + 1] - block[i]))

	return np.array([res])

# save plot for the visualization
def plotAction(stock_name, buy_data, sell_data, model_name):
	stock_data = pd.read_csv("data/" + stock_name + ".csv")
	buy_data = np.array(buy_data)
	sell_data = np.array(sell_data)
	l = len(stock_data['Date'])
	t = np.arange(0,l,1)

	fig, ax = plt.subplots(figsize=(18,8))
	ax.plot(t, stock_data['Close'], label=str(stock_name), color = 'grey')
	ax.plot(buy_data[:, 0], buy_data[:, 1],'go', markersize = 4.5, label='Buy')
	ax.plot(sell_data[:, 0], sell_data[:, 1], 'ro', markersize = 4.5, label='Sell')

	legend = ax.legend(loc='upper right')
	plt.savefig('plots/'+str(stock_name)+'_'+str(model_name)+'.png', dpi=200)

