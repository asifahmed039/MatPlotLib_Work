#subplot(nrows,ncols,index) for multiple plot in single screen.


import matplotlib.pyplot as plt
#set1
hours_studies=[1,2,5,6,4,3,7,8]
exam_scores=[50,55,60,70,65,80,85,45]
#set2
hours_studies2=[1,2,5,6,4,3,7,8]
exam_scores2=[58,55,68,35,55,90,75,65]

#sublpot
plt.subplot(1,2,1)
#scatter plot
plt.plot(hours_studies,exam_scores,color='red',marker='o',label='class A')
plt.title("line chart")

plt.subplot(1,2,2)
plt.scatter(hours_studies2,exam_scores2,color='blue',marker='o',label='class B')
plt.title('report card')
plt.xlabel='hours'
plt.ylabel='scores'
plt.legend(loc='lower right')
plt.grid(True)
plt.show()