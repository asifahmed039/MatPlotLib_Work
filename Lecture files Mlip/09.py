#through object subgroup concept.
#fig, ax=plt.subplot(nrows,ncols,figsize=(width,height))
import matplotlib.pyplot as plt
fig, ax=plt.subplots(1,2,figsize=(10,5,))

hours_studies=[1,2,5,6,4,3,7,8]
exam_scores=[50,55,60,70,65,80,85,45]

ax[0].plot(hours_studies,exam_scores,color="red")
ax[0].set_title('line chart')


ax[1].bar(hours_studies,exam_scores,color="green")
ax[1].set_title('bar chart')

fig.suptitle('Comparison of line and bar chars.',color="red")

plt.tight_layout()
plt.show()
