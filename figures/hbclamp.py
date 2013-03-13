import pylab
def HBclassic(par,shear):
    return (par[0]+par[1]*shear**par[2])/shear
def HBclamp(upper,lower):
    return clip(HBclassic(parMaxA,x),lower,upper)

fontSizeTicks=14
fontSizeLabel=17
fontSizeLegend=16

parMaxA = [199.983, 60.89914, 0.621]
x=logspace(-7,7,100)

fig = pylab.figure(figsize=(12,4))
ax= fig.add_subplot(111)

pylab.loglog(x,HBclassic(parMaxA,x),'r--',label='Herschel-Bulkley Modell')
pylab.loglog(x,HBclamp(1e7,1e0),label='limitiertes Herschel-Bulkley Modell')

pylab.rcParams['mathtext.default']='regular'

pylab.xlabel('Scherrate / $s^{-1}$',fontsize=fontSizeLabel)
pylab.ylabel('Viskosit$\ddot a$t / Pa s',fontsize=fontSizeLabel)
pylab.legend(prop={'size':fontSizeLegend})

pylab.setp(ax.get_xticklabels(), fontsize=fontSizeTicks)
pylab.setp(ax.get_yticklabels(), fontsize=fontSizeTicks)
pylab.tight_layout()

pylab.savefig('/home/simon/Documents/ETH/Master-Thesis/Thesis/figures/hbclamp.png')
