from scipy.misc import factorial

def modHB(par,x):
    return (par[0]*(1-exp(-1000*x)) + par[1]*x**par[2])/x
def HB(par,x):
    return par[0]/x + par[1]* x**(par[2]-1)
def dilatantMod(par,x):
    return par[0]+factorial(x**(1./par[1]))
def carreauModell(par,x):
    return par[0]+(par[1]-par[0])*(1+x**par[2])**((par[3]-1)/par[2])
def sikoModell(par,x):
    return par[0]+par[1]*x**(par[2]-1)


parSet1 = [0,1e2,1] # HB - Newtonsch
parSet2 = [1e2,10.5] # Dilatant
parSet3 = [1e1,1e2,1,0.1] # Carreau - Scherverduennend
parSet4 = [1e1,1e2,0.1] # Plastic

x = logspace(-3,4,100)

# Newtonsch
newtLeg = 'Newtonsch'
newt,=loglog(x,modHB(parSet1,x),'k',label=newtLeg)

# Viskoplastisch
plasticLeg = 'Viskoplastisch'
plastic,=loglog(x,sikoModell(parSet4,x),'g',label=plasticLeg)

# Dilatant
dilLeg = 'Dilatant'
dil,=loglog(x,dilatantMod(parSet2,x*1e4),'b',label=dilLeg)

# Scherverduennend
scherLeg = 'Strukturviskos'
scher,=loglog(x,carreauModell(parSet3,x),'r-',label=scherLeg)

#legend([newt,dil,scher,newt],[newtLeg,dilLeg,scherLeg,plasticLeg])
legend(loc='lower left')
xlabel('Scherrate')
ylabel("Viskosit$\ddot{a}$t")
ylim([5e0,1e3])
savefig('fliesskurven.png',bbox_inches=0)
