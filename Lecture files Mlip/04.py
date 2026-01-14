#bar-----histogram-------pichart
import matplotlib.pyplot as plt

product=["A","B","C","D"]
sales=[1000,1500,800,1400]
plt.barh(product,sales,color=['red','blue','green','gray'], label="Sales 2025")    #or plt.bar() for vertically
plt.title('Product sale comparison')
plt.xlabel("product")
plt.ylabel("sales")
plt.legend()
plt.show()