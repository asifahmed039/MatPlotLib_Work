#scatter plot
"""
    plt.scatter(x,y,color='color_name',marker='marker_style',label='label_name)

    why its use 
    find co relation b/w to two variable 
    use for prediction in machine learning.
    [*]color psychology learn 

"""
import matplotlib.pyplot as plt
hours_studies=[1,2,5,6,4,3,7,8]
exam_scores=[50,55,60,70,65,80,85,45]

#scatter plot
plt.scatter(hours_studies,exam_scores,color='green',marker='o',label='Student data')
plt.title='report card'
plt.xlabel='hours'
plt.ylabel='scores'
plt.legend(loc='lower right')
plt.grid(True)
plt.savefig('scatter.png',dpi=300,bbox_inches='tight')
plt.show()