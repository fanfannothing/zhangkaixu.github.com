#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


class Fun :
    def __init__(self):
        self.x=0.8
        self.y=0.5
        self.x2=-0.8
        self.y2=0.8
        self.k=1.2
    def _f1(self,x,y):
        return np.exp(-((x*2-self.x)**2+(y-self.y)**2))
    def _f2(self,x,y):
        return np.exp(-((x*2-self.x2)**2+(y-self.y2)**2))

    def f(self,x,y):
        f1=self._f1(x,y)
        f2=self._f2(x,y)
        return  f2*self.k+f1

    def f_prime(self,x,y):
        f1=-self._f1(x,y)
        f2=-self._f2(x,y)
        return (f1*-1*2*((2*x-self.x))+ f2*-2*(2*x-self.x2)*self.k, 
                f1*-1*(y-self.y) + f2*-1*(y-self.y2)*self.k
                )


def sgd(fun,x0,y0):
    eta=1.2
    xs=[x0]
    ys=[y0]
    for i in range(20):
        tx,ty=fun.f_prime(x0,y0)
        x0-=eta*tx
        y0-=eta*ty
        xs.append(x0)
        ys.append(y0)
    return xs,ys
        


x=np.arange(-1,1,0.01)
y=np.arange(-1,1,0.01)
X,Y=np.meshgrid(x,y)


fun=Fun()
Z=fun.f(X,Y)

levels=[0.5,0.8,1,1.1,1.2]
x0=0
y0=-1
xs,ys=sgd(fun,x0,y0)

plt.figure(figsize=(4,3))

cs=plt.contour(X,Y,Z,levels)
plt.clabel(cs,fontsize=10)

for i in range(len(xs)-1):
    plt.arrow(xs[i],ys[i],(xs[i+1]-xs[i])/2,(ys[i+1]-ys[i])/2,head_width=0.03,head_length=0.05)

plt.plot(xs,ys,'.')

plt.xlim(-1,1)
plt.ylim(-1,1)
plt.grid()
plt.show()
#plt.savefig("test.png")
