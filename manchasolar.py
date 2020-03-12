from pylab import plot,show,xlim,ylim,xlabel,ylabel
from numpy import linspace,sin,cos,loadtxt,zeros


a=loadtxt("sunspots.txt",float)
#plot(a[:,0],a[:,1])

r=5
y_2=zeros(1000,float)
for k in range (0,1000):
    for m in range(-r,r):
        y_2[k]+=a[k+m,1]
    y_2[k]/=2*r+1

plot(a[:,0],a[:,1],"g", label="grafica normal")
plot(a[0:1000,0],y_2,"r",label="NOrmalizada")

xlim(0,1001)
xlabel("mes")
ylabel("numero de manchas")
#legend()
show()
 
