import matplotlib.pyplot as plt

fig=plt.figure()
rect=fig.patch
rect.set_facecolor('lightgoldenrodyellow')

ax1=fig.add_axes([0.1,0.3,0.4,0.4])
rect=ax1.patch
rect.set_facecolor('lightslategray')

for label in ax1.xaxis.get_ticklabels():
    label.set_color('tab:red')
    label.set_rotation(45)
    label.set_fontsize(16)

for line in ax1.yaxis.get_ticklines():
    line.set_color('tab:green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)

plt.show()
