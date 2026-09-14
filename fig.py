import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
plt.rcParams.update({'font.size':9,'font.family':'serif','axes.linewidth':0.7})

w=[(6,8),(8,12),(12,14),(14,18),(18,20),(20,24),(24,28)]
uns=[(2.25,2.75),(2.75,3.0),(3.0,3.75),(3.75,4.25),(4.25,4.5),(4.5,5.0),(5.0,5.5)]
stf=[(2.75,3.0),(3.0,3.5),(3.5,4.0),(4.0,4.25),(4.25,4.75),(4.75,5.25),(5.25,5.75)]
g=lambda p:np.array([np.sqrt(a*b) for a,b in p])
m,tu,ts=g(w),g(uns),g(stf)
xe=np.array([[np.sqrt(a*b)-a,b-np.sqrt(a*b)] for a,b in w]).T
yu=np.array([[np.sqrt(a*b)-a,b-np.sqrt(a*b)] for a,b in uns]).T
ys=np.array([[np.sqrt(a*b)-a,b-np.sqrt(a*b)] for a,b in stf]).T

fig,ax=plt.subplots(1,3,figsize=(9.6,3.0))

# (a) donnees + ajustement
a0=ax[0]
a0.errorbar(m,tu,xerr=xe,yerr=yu,fmt='o',ms=4,lw=.8,capsize=2,color='#1b3a6b',label='unstuffed')
a0.errorbar(m,ts,xerr=xe,yerr=ys,fmt='s',ms=4,lw=.8,capsize=2,color='#b4472a',mfc='none',label='stuffed')
mm=np.linspace(5.5,30,100)
s,i=np.polyfit(np.log(m),np.log(tu),1)
a0.plot(mm,np.exp(i)*mm**s,'-',color='#1b3a6b',lw=1.1)
a0.plot(mm,tu[0]*(mm/m[0])**(2/3),'--',color='k',lw=.9,label=r'$n=2/3$')
a0.plot(mm,tu[0]*(mm/m[0])**1,':',color='gray',lw=1.1,label=r'$n=1$')
a0.set_xscale('log');a0.set_yscale('log')
a0.set_xlabel('mass (lb)');a0.set_ylabel('roasting time (h)')
a0.set_xticks([6,10,15,20,30]);a0.set_yticks([2,3,4,5,6])
a0.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
a0.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
a0.legend(frameon=False,fontsize=7.5,loc='upper left')
a0.set_title('(a) chart data, log--log',fontsize=9,loc='left')

# (b) r(m^x, t) : non discriminant
a1=ax[1]
xs=np.linspace(0.25,1.15,120)
a1.plot(xs,[np.corrcoef(m**x,tu)[0,1] for x in xs],color='#1b3a6b')
a1.set_ylim(0.9,1.005);a1.axvline(2/3,ls='--',c='k',lw=.8);a1.axvline(0.5,ls=':',c='gray',lw=.9)
a1.set_xlabel(r'assumed exponent $x$');a1.set_ylabel(r'$r(m^{x},\,t)$')
a1.text(0.30,0.925,'full range spans\n$\\Delta r < 0.004$',fontsize=7.5)
a1.set_title('(b) correlation cannot discriminate',fontsize=9,loc='left')

# (c) exposant effectif vs Bi
def L1(Bi): return brentq(lambda L:1-L/np.tan(L)-Bi,1e-6,np.pi-1e-9)
def A1(Bi):
    L=L1(Bi);return 2*(np.sin(L)-L*np.cos(L))/(L-np.sin(L)*np.cos(L))
th=0.560
def Fo(Bi): return np.log(A1(Bi)/th)/L1(Bi)**2
Bi=np.logspace(-0.5,2.5,200)
neff=[]
for B in Bi:
    d=1e-3
    dlnFo=(np.log(Fo(B*(1+d)))-np.log(Fo(B*(1-d))))/(2*d)
    neff.append((2+dlnFo)/3)
a2=ax[2]
a2.semilogx(Bi,neff,color='#1b3a6b')
a2.axhline(2/3,ls='--',c='k',lw=.8);a2.text(60,0.672,'$2/3$',fontsize=8)
a2.axhspan(0.52,0.56,color='#b4472a',alpha=.16)
a2.text(0.4,0.535,'measured\n$n=0.54\\pm0.02$',fontsize=7.5,color='#8a3520')
a2.axvspan(2,8,color='gray',alpha=.14)
a2.text(2.3,0.30,'turkey\nrange',fontsize=7.5,color='dimgray')
a2.set_xlabel('Biot number  $Bi=hl/k$');a2.set_ylabel(r'effective exponent $n$')
a2.set_ylim(0.25,0.70)
a2.set_title('(c) finite-$Bi$ prediction',fontsize=9,loc='left')

for a in ax: a.tick_params(direction='in',top=True,right=True,which='both')
plt.tight_layout();plt.savefig('fig1.pdf',bbox_inches='tight');print("ok")
