#histogram
import matplotlib.pyplot as plt
score=[45,64,89,56,78,88,92,60,74,81,59,66,75,82,90,85,70,73,68,77]
plt.hist(score,bins=5,color='blue',edgecolor='black')
plt.ylabel('score range')
plt.title('Score distribution of student')
plt.show()

