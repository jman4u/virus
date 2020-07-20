from visualize import *

file1 = open("high_scores1.csv", "r")
file2 = open("high_scores2.csv", "r")
file3 = open("high_scores3.csv", "r")

data1 = []
data2 = []
data3 = []


for line in file1:
  if line != "":
    line = int(line.strip())
    data1.append(line)
  
for line in file2:
  if line != "":
    line = int(line.strip())
    data2.append(line)

for line in file3:
  if line != "":
    line = int(line.strip())
    data3.append(line)    
    
f = figure(x_range = (-1,5), y_range = (0,60))
#define axes
f.xaxis.axis_label = "strat1, strat2, strat3"
f.xaxis.axis_label_text_font_size = "20px"
f.yaxis.axis_label = "seconds to infect all"
f.yaxis.axis_label_text_font_size = "20px"


#box and whisker plot:

box_whisker_plot(data1,0, "green",f)
box_whisker_plot(data2,1,"blue",f)
box_whisker_plot(data3,2,"yellow",f)


show(f)

