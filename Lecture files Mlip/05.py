#pichart
import matplotlib.pyplot as plt

region=['north','south','east','west']
revenue=[1000,3000,4000,600]
plt.pie(revenue, labels=region,autopct='%1.1f%%',colors=['green','yellow','blue',"red"])
plt.title("Revenue report")
plt.legend(loc='lower right')
plt.show()