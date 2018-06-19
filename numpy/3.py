dates, price, close=np.loadtxt('prices.csv', delimiter=',', usecols=(0,2,3), converters={1: dates2num}, unpack=True, dtype='str')
