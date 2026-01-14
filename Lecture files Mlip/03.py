#
"""
    home work-----
    color,linestyle,linewidth,marker,symbol,label    use in plot() function
"""
import matplotlib.pyplot as plt

months=[1,2,3,4]
sales=[1000,2000,3000,1800]

plt.plot(months,sales, color="green",linestyle="--",marker="o",label="2025 sales data")
plt.xlabel("months")   # x- axis label
plt.ylabel("sales")     #y axis lebal
plt.title("monthly sales data report.")   #title
plt.legend(loc="lower right",fontsize=12)
plt.grid(color="gray",linewidth=1,linestyle="--")
plt.xlim(1,4)
plt.ylim(0,3000)
plt.xticks([1,2,3,4],["m1","m2","m3","m4"])



plt.show()

