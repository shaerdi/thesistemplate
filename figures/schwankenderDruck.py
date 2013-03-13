import numpy as np
import pylab

p = np.loadtxt('schwankenderDruck.dat')
p[:,1] = p[:,1]*1470./100000. # Convert to Bar

fontSizeTicks=14
fontSizeLabel=16
#fontSizeLegend=16

fig = pylab.figure(figsize=(12,4))
ax = fig.add_subplot(111)

ax.plot(p[:,0],p[:,1])
ax.set_xlim(right=0.2)

pylab.rcParams['mathtext.default']='regular'

pylab.xlabel('t / s',fontsize=fontSizeLabel)
pylab.ylabel('Einlassdruck / Bar',fontsize=fontSizeLabel)

pylab.setp(ax.get_xticklabels(), fontsize=fontSizeTicks)
pylab.setp(ax.get_yticklabels(), fontsize=fontSizeTicks)

pylab.tight_layout()

pylab.savefig('/home/simon/Documents/ETH/Master-Thesis/Thesis/figures/schwankenderDruck.png')
