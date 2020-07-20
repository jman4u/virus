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


class Cell:
  def __init__(self, color):
    self.position = Point(random.randint(7,793),random.randint(7,593))
    self.size = 7
    self.color = color
    self.vel = Vector(random.uniform(-2,2),random.uniform(-2,2))

  def moving(self, cells):
    if self.position.x >= 796.5:
      self.vel.h *= -1
    if self.position.x<=3.5:
      self.vel.h *= -1
    if self.position.y >= 596.5:
      self.vel.v *=-1
    if self.position.y <= 3.5:
      self.vel.v *=-1
      
    for othercell in cells:
      dist = self.position.distance(othercell.position)
      if dist < 7:
        if self.color == "green" and othercell.color == "red":
          self.color = "red"

    #this code just prevents cell from going faster than 2 pixels a frame
    if self.vel.length() >= 2:
      self.vel.normalize()
      self.vel.multiply(2)
      
    self.position.move(self.vel)
  
  def drawing(self):
    if self.color == "green":
      fill(0,255,0)
    else:
      fill(255,0,0)
    ellipse(self.position.x,self.position.y,7,7)
    

class Epidemic:
  def __init__(self,num):
    self.num = num
    self.redc = 0
    self.timer = 0
    self.times = 0
    self.framerate = 60

    
    cells.append(Cell("red"))

    for i in range(self.num):
      cells.append(Cell("green"))
      
  def strat1(self):
    self.redc = 0

    for cell in cells:
      if cell.color == "red":
        self.redc+=1
      cell.moving(cells)
      cell.drawing()
      
    self.timer +=1


    #this will look weird unless completely randomized again
    if self.redc>=self.num:
      if self.times <=50:
        f.write(str(int(self.timer/self.framerate)) + "\n")
      self.times +=1
      self.timer = 0
      for i in range(len(cells)):
        cells.pop(0)
      cells.append(Cell("red"))
      for i in range(self.num):
        cells.append(Cell("green"))
        
      
      
  def strat2(self):
    self.redc = 0

    for cell in cells:
      if cell.color == "red":
        self.redc+=1
        #unique part 
        for othercell in cells:
          if cell.position.distance(othercell.position)<50 and othercell.color == "green":
            vec = cell.position.makeVectorTo(othercell.position)
            vec.normalize()
            vec.multiply(2)
            cell.vel = vec
            break
      cell.moving(cells)
      cell.drawing()

    self.timer +=1

    #this will look weird unless completely randomized again
    if self.redc>=self.num:
      if self.times <=50:
        f.write(str(int(self.timer/self.framerate)) + "\n")
      self.times +=1
      self.timer = 0
      for i in range(len(cells)):
        cells.pop(0)
      cells.append(Cell("red"))
      for i in range(self.num):
        cells.append(Cell("green"))
    
      
  def strat3(self):
    #this strategy will be forming two horizontal lines in the middle of the screen to catch cells
    #while also putting a limit on the cells in these lines to allow some to chase
    self.redc = 0
    self.linec1 =0
    self.linec2 =0

    for cell in cells:
      if cell.color == "red":
        self.redc+=1
        #unique part 
        if cell.position.y >390 and cell.position.y <410 and self.linec1<20:
          cell.vel = Vector(cell.vel.h,0)
          self.linec1 +=1
        elif cell.position.y >190 and cell.position.y <210 and self.linec2<20:
          cell.vel = Vector(cell.vel.h,0)
          self.linec2 +=1
        else:
          for othercell in cells:
            if cell.position.distance(othercell.position)<50 and othercell.color == "green":
              vec = cell.position.makeVectorTo(othercell.position)
              vec.normalize()
              vec.multiply(2)
              cell.vel = vec
              break
      cell.moving(cells)
      cell.drawing()
      
    self.timer +=1
  
    #this will look weird unless completely randomized again
    if self.redc>=self.num:
      if self.times <=50:
        f.write(str(int(self.timer/self.framerate)) + "\n")
      self.times +=1
      self.timer = 0
      for i in range(len(cells)):
        cells.pop(0)
      cells.append(Cell("red"))
      for i in range(self.num):
        cells.append(Cell("green"))
    

cells = []
virus1 = Epidemic(100)


#f = open("high_scores1.csv","a")
#f = open("high_scores2.csv","a")
#f = open("high_scores3.csv","a")


def setup():
  size(800,600)

  
def draw():
  background(255)
  
  #uncomment the strategy you want to use
  #virus1.strat1()
  #virus1.strat2()
  #virus1.strat3()
  

#run()  