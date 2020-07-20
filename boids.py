from processing import *
import math
import random

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def distance(self, point):
        return ((self.x-point.x)**2+(self.y-point.y)**2)**.5
    
    
    def move(self,vector):
        self.x += vector.h
        self.y += vector.v
        
    def makeVectorTo(self, point):
      x_change = point.x - self.x
      y_change = point.y - self.y
      return Vector(x_change, y_change)
    
    

class Vector:
    def __init__(self, h, v):
        self.h = float(h)
        self.v = float(v)
        
    def add(self, otherVector):
        self.h += otherVector.h
        self.v += otherVector.v
        
    def subtract(self, otherVector):
        self.h -= otherVector.h
        self.v -= otherVector.v
   
    def multiply(self, scalar):
        self.h *= scalar
        self.v *= scalar
   
    def divide(self, scalar):
        if scalar != 0:
            self.h /= scalar
            self.v /= scalar
    
    def length(self):
      return (self.h**2+self.v**2)**.5
    
    def normalize(self):
        self.divide(self.length())


class Boid:
  def __init__(self):
    self.position = Point(random.randint(7,793),random.randint(7,593))
    self.color = random.choice(["green","red","blue"])
    self.vel = Vector(0,0)

  def update(self):
    
    self.scaling = 3
    self.vscal = self.scaling*-1
    
    #edge avoidance - will just make it change velocities in one component
    if self.position.x >= 760:
      self.vel.h += self.vscal
    if self.position.x<=40:
      self.vel.h -= self.vscal
    if self.position.y >= 560:
      self.vel.v += self.vscal
    if self.position.y <= 40:
      self.vel.v -= self.vscal
      
      
    #separation
    counta = 0
    countc = 0
    alignvector = Vector(0,0)
    cohesavgpos = Point(0,0)
    for otherboid in boids:
      dist = self.position.distance(otherboid.position)
      if dist < 25 and self.position.x != otherboid.position.x and self.position.y != otherboid.position.y:
        newvector = otherboid.position.makeVectorTo(self.position)
        newvector.divide(dist**2)
        newvector.multiply(15)
        self.vel.add(newvector)
    
      #alignment
      elif dist < 45:
        alignvector.add(otherboid.vel)
        counta +=1
      #cohesion
        cohesavgpos.x += otherboid.position.x
        cohesavgpos.y += otherboid.position.y
        countc +=1
    
    #alignment part again:
    alignvector.divide(counta)
    alignvector.multiply(.3)
    self.vel.add(alignvector)
    #cohesion part again:
    cohesavgpos.x /= countc
    cohesavgpos.y /= countc
    cohesvector = self.position.makeVectorTo(cohesavgpos)
    cohesvector.multiply(.05)
    self.vel.add(cohesvector)
    
    #speed limit
    if self.vel.length() > 3:
      self.vel.normalize()
      self.vel.multiply(3)

    self.position.move(self.vel)
  
  def shape(self):
    if self.color == "green":
      fill(0,255,0)
    elif self.color == "red":
      fill(255,0,0)
    else:
      fill(0,0,255)
    ellipse(self.position.x,self.position.y,7,7)
    

class Simulation:
  def __init__(self,num):
    self.num = num
    self.timer = 0
    self.framerate = 60

    for i in range(self.num):
      boids.append(Boid())
      
  def strat1(self):

    for boid in boids:
      boid.update()
      boid.shape()
      
    self.timer +=1

        

boids = []
boids1 = Simulation(100)


def setup():
  size(800,600)

  
def draw():
  background(255)
  boids1.strat1()
  

#run()  