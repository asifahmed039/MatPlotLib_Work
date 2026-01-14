import matplotlib.pyplot as plt
x=['Mon','Tue','Wed','Thr','Fri']   #x-Axis
y=[10,15,7,25,13]    #y-axis
plt.plot(x,y)
plt.title("Sales report")
plt.xlabel("Day")
plt.ylabel("sales per day")
plt.show()