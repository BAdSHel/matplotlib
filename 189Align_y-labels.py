import numpy as np
import matplotlib.pyplot as plt

def make_plot(axs):
    box=dict(facecolor='yellow',pad=5, alpha=0.2)

    np.random.seed(19680801)
    ax1=axs[0,0]
    ax1.plot(2000*np.random.rand(10))
    ax1.set_title('ylabels not aligned')
    ax1.set_ylabel('misaligned 1',bbox=box)
    ax1.set_ylim(0,2000)

    ax3=axs[1,0]
    ax3.set_ylabel('misaligned 2',bbox=box)
    ax3.plot(np.random.rand(10))

    ax2=axs[0,1]
    ax2.set_title('ylabel aligned')
    ax2.plot(2000*np.random.rand(10))
    ax2.set_ylabel('aligned 1', bbox=box)
    ax2.set_ylim(0,2000)

    ax4=axs[1,1]
    ax4.plot(np.random.rand(10))
    ax4.set_ylabel('aligned 2', bbox=box)

fig, axs=plt.subplots(2,2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

fig.align_ylabels(axs[:,1])
plt.show()


fig, axs=plt.subplots(2,2)
fig.subplots_adjust(left=0.2,wspace=0.6)

make_plot(axs)

labelx=-0.3

for j in range(2):
    axs[j,1].yaxis_set_label_coords(labelx,0.5)

plt.show()

