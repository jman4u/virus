import numpy as np
import math
import random
from bokeh.plotting import figure, show


def box_whisker_plot(data,x, colors, name):
  #makes the vertical bar
  name.vbar(x = x, top = np.percentile(data,75), bottom = np.percentile(data,25), width = .8, color = colors)
  #lines for outliers, connecting to 25/75 percentiles, median
  #the first array is what x values the line will cover; the second is what y values the line will cover
  name.line([x-.2, x+.2],[min(data), min(data)])
  name.line([x-.2, x+.2],[max(data), max(data)])
  name.line([x,x], [min(data), np.percentile(data, 25)])
  name.line([x,x], [np.percentile(data,75), max(data)])
  #line for median now
  name.line([x-.4, x+.4], [np.percentile(data, 50), np.percentile(data, 50)], line_width = 2, line_color = "black")

def histogram(data,binSize,barWidth,colors,name):
  high = -10000000000.1
  for i in data:
    if i >high:
      high = i
  hist = np.histogram(data, bins = binSize+1, range = (0, high))
  yVals = hist[0]
  xVals = hist[1]
  xVals = xVals[0:-1] + (xVals[0] + xVals[1])/2
  for (x,y) in zip(xVals, yVals):
    w = (xVals[0] + xVals[1])/2
    name.vbar(x, w*barWidth,y,0)

def pieChart(data, titles, colors, x, y, name):
  total = sum(data)
  data.insert(0,0)
  data = np.array(data)
  data_angles = data * 2 *math.pi / total
  angle_cum = np.cumsum(data_angles)
  #protect from index out of bounds
  for i in range(len(angle_cum)-1):
    name.annular_wedge(x,y,0,2,angle_cum[i], angle_cum[i+1],color = colors[i])
    #if you want more texts to appear on graph besides about 8, extend figure range
    name.text(x + 3, 7-i, [titles[i]])
    name.circle([x+3.5], [7 -i], size = 15, color = colors[i])

def scattergram(x,y,dot_size,colors,name):
  name.circle(x,y,size = dot_size,color = colors)
  
