import random

def axes():
    strokeWeight(3)
    stroke(90)
    line(0,-height/2,0,height/2)
    line(-width/2,0,width/2,0)

s = 10
xscl = 15.0
yscl = 20.0
x = range(-50,50,1)
domain = len(x)
y = [0]*domain
y2 = [0]*domain
w = [0]*s
o = [0]*s
a = [0]*s

def func(x):
    q=0
    while q<s-4:
        w[q] = random.uniform(0.05,0.2)
        o[q] = random.uniform(-30,30)
        a[q] = random.uniform(1,3.5)
        q+=1
    while q<s:
        w[q] = random.uniform(0.005,0.1)
        o[q] = random.uniform(-40,40)
        a[q] = random.uniform(1,6)
        q+=1
    i=0
    while i<domain-1:
        f=0
        while f<s:
            y[i] += a[f]*exp(-(w[f]*(x[i]-o[f]))**2)
            f+=1
        i+=1
    print(a)
        
        
def graph():
    func(x)
    j=0
    noFill()
    #beginShape()
    while j<domain:
        #ellipse(xscl*x[j],-yscl*y[j],4,4)
        if j>0:
            line(xscl*x[j],-yscl*y[j],xscl*x[j-1],-yscl*y[j-1])
        j+=1
    #endShape()

def setup():
    size(1300,800)
    noLoop()
    
def draw():
    translate(width/2, height/2)
    background(255)
    
    axes()
    graph()
    
    

    
