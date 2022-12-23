from algebra import *
import random

def f(t):
    fx=algebra_expression([1,0])
    for n in range(t):
        fx=add(multiply(fx,fx),algebra_expression([1,0]))
    return fx

def g(t0,t1):
    if t0==0:
        fx=f(t0+t1-1)
    else:
        fx=add(f(t0+t1-1),f(t0-1))
    #print(t0,t1,fx.toString())
    factors=[]
    for t in range(1,t1+1):
        if t1%t==0:
            factors.append(t)
    for factor in factors:
        for t in range(t0+1):
            if factor!=t1 or t!=t0:
                gx,hx=devide(fx,g(t,factor))
                #print(hx.coefficients)
                if hx.coefficients==[0]:
                    fx=gx
    return fx

if __name__=='__main__':
    fx=g(4,1)
    print(fx.toString())
    ans=[]
    if len(fx.coefficients)<4:
        ans=solve(fx)
    if len(ans)==0:
        ans1=[]
        gx=fx
        while len(gx.coefficients)>1:
            x,d,y=newton(gx,random.uniform(-2,2)+random.uniform(0,2)*1j)
            if abs(y)<2**-32:
                if type(x)==float:
                    gx=devide(gx,algebra_expression([1,-x]))[0]
                    ans1.append(x)
                else:
                    gx=devide(gx,algebra_expression([1,-2*x.real,abs(x)**2]))[0]
                    ans1.append(x)
                    ans1.append(x.conjugate())
        for a in ans1:
            ans.append(newton(fx,a)[0])
    print(ans)
    '''for t in range(1,7):
        for t0 in range(t):
            t1=t-t0
            fx=g(t0,t1)
            print(fx.toString())
            ans=[]
            if len(fx.coefficients)<4:
                ans=solve(fx)
            if len(ans)==0:
                ans1=[]
                gx=fx
                while len(gx.coefficients)>1:
                    x,d,y=newton(gx,random.uniform(-2,2)+random.uniform(0,2)*1j)
                    if abs(y)<2**-32:
                        if type(x)==float:
                            gx=devide(gx,algebra_expression([1,-x]))[0]
                            ans1.append(x)
                        else:
                            gx=devide(gx,algebra_expression([1,-2*x.real,abs(x)**2]))[0]
                            ans1.append(x)
                            ans1.append(x.conjugate())
                for a in ans1:
                    ans.append(newton(fx,a)[0])
            print(ans)
            import cv2
            import numpy as np
            img=cv2.imread('Mandelbrot_1024.png')
            for a in ans:
                cv2.circle(img,(int(a.real*256+512),int(-a.imag*256+512)), 2, (0,0,255), 1)
            cv2.imwrite('Mandelbrot_'+str(t0)+'_'+str(t1)+'.png',img)'''