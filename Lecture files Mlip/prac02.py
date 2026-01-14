import matplotlib.pyplot as plt
country_area=[17.09,9.98,9.83,9.60,8.51,7.69,3.28]
country_name=['Russia','Canada','USA','China','Brazil','Australia','India']
plt.bar(country_name,country_area)
plt.title('Seven largest countries of World',fontsize=15,color='red')
plt.xlabel('Country',color='green')
plt.ylabel('Area(In sq km)',color='green')
plt.legend()
plt.show()
