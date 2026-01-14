import matplotlib.pyplot as plt
stock=[115.50,116.25,119.55,113.23,117.55,120.95]
days=['mon','tue','wed','thrus','fri','sat']
plt.plot(days,stock,color='red',marker='o')
plt.legend(loc='lower right')
plt.grid()
plt.show()
sales=[500000,1000000,200000,30000]
months=['march','april','may','june']


plt.pie(sales,labels=months,autopct='%1.1f%%',colors=['green','red','blue','gray'])

plt.show()