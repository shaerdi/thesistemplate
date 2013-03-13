from scipy.misc import factorial
import pylab

def carreauModell(par,x):
    return par[0]+(par[1]-par[0])*(1+x**par[2])**((par[3]-1)/par[2])


parSet3 = [2e0,1e2,1,0.1] # Carreau - Scherverduennend

x = logspace(-3,4,100)
s = carreauModell(parSet3,x)
n = np.size(x)

fig = pylab.figure(figsize=(12,4))
ax = fig.add_subplot(111)
lw = 3.0
fontSizeTicks=14
fontSizeLabel=16
fontSizeLegend=16

# Scherverduennend
scherLeg = 'Strukturviskos'
scher,=pylab.loglog(x,s,'r-',label=scherLeg,linewidth=lw)

pylab.rcParams['mathtext.default']='regular'

pylab.xlabel('Scherrate $\dot \gamma$ / $s^{-1}$',fontsize=fontSizeLabel)
pylab.ylabel("Viskosit$\ddot{a}$t $\eta$ / $Pa\cdot s$",fontsize=fontSizeLabel)
pylab.ylim([1e0,2e2])
pylab.setp(ax.get_xticklabels(), fontsize=fontSizeTicks)
pylab.setp(ax.get_yticklabels(), fontsize=fontSizeTicks)

plotn=n/5
ax.annotate('Plateau bei niedrigen Scherraten', xy=(x[plotn], s[plotn]), xytext=(0.002, 30),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            fontsize = fontSizeLegend
            )
plotn=5*n/9
ax.annotate('Exponentieller $\ddot U$bergang', xy=(x[plotn], s[plotn]), xytext=(0.1, 5),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            fontsize = fontSizeLegend
            )
plotn=6*n/7
ax.annotate('Plateau bei hohen Scherraten', xy=(x[plotn], s[plotn]), xytext=(60,10),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            fontsize = fontSizeLegend
            )

pylab.tight_layout()
pylab.show()
pylab.savefig('/home/simon/Documents/ETH/Master-Thesis/Thesis/figures/CarreauYasudaAnnotated.png',bbox_inches=0)

