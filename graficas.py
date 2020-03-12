from pylab import plot,show,xlim,ylim,xlabel
from numpy import linspace,sin,cos,loadtxt



#x=[]
#y=[]


#for i in range (10):
 #   y.append(i*i)
  #  x.append(2*i)
#plot(x,y)


x=linspace(0,10,100)
#print(x)
y=sin(x)
z=cos(x)
#plot(z,w)
#show()

a=open("test.dad", "w")
for i in range (len(x)):
    a.write("%.2f %.2f %.2f\n" % (x[i], y[i],z[i]))
a.close()

b=loadtxt("test.dad",float)
#plot(x,y)
plot(b[:,0], b[:,1],"go")
plot(b[:,0], b[:,2],"r-")

ylim(-1.01, 1.1)
xlabel("Radianes")
show()


