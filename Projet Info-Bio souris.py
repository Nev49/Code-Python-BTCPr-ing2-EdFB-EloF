from matplotlib import pyplot as plt
import pandas as pd
import math
import matplotlib.patches as mpatches
import shutil
import os


figure1, axis1 = plt.subplots()
figure2, axis2 = plt.subplots()
figure3, axis3 = plt.subplots()


### Extraction of mice IDs in the CSV file ####

def mice_id():
    data = pd.read_csv("data_small.csv", sep=";")
    return data.iloc[:, 4].unique()

#### Fecal graphic ####

def graphic_basic (x,y,) :
  #for mouse_id in mice :      
      clr = "#0000FF"
      if treatment == "ABX" :
          clr = "#FF0000"

      axis1.set_title('Live Bacteria Counts Over Time by Mouse and Treatment', fontsize= 13)

      #Put the legend on the graphic
      ABX = mpatches.Patch(color='#F35D5DFF', label='ABX')
      PLA = mpatches.Patch(color='#5182CC', label='Placebo')
      axis1.legend(handles=[ABX, PLA], loc="upper right")
      
      axis1.set_xlabel('Washout day', fontsize=10)
      axis1.set_ylabel('Log10 of Live Bacteria per Wet Gram of Feces', fontsize=10)
      
      axis1.plot(x, y, color=clr, alpha=0.5)      
      
      figure1.legend(loc="right")
      figure1.savefig("Basic_fecal_figure.png", dpi=150)

#### Cecal violin graphic ####

def violin_graphic_cecal (x2, y2, treat) :
    axis2.set_title("Cecal live bacteria", fontsize = 13)
    
    #Put the legend on the graphic
    ABX = mpatches.Patch(color='#F35D5DFF', label='ABX')
    PLA = mpatches.Patch(color='#5182CC', label='Placebo')
    axis2.legend(handles=[ABX, PLA], loc="lower right")
    
    #Name the axes
    axis2.set_xlabel("treatment", fontsize = 10)
    axis2.set_ylabel("log10(live bacteria/wet g)", fontsize = 10)
        
        
    vp=axis2.violinplot([x2,y2])
    #axis.scatter(x2, y2, marker="x")

    #Colors of the graphic
    colors=['#5182CC', '#F35D5DFF']
    edge_colors=['#0000FF', '#FF0000']
    
    for i, body in enumerate(vp['bodies']):
        body.set_facecolor(colors[i])
        body.set_edgecolor(edge_colors[i])
    
    figure2.legend(loc="right")
    figure2.savefig("Violin_cecal_figure.png", dpi=150)

#### Ileal violin graphic ####

def violin_graphic_ileal (x3, y3, treat) :
    axis3.set_title("Ileal live bacteria", fontsize = 13)
    
    #Put the legend on the graphic
    ABX = mpatches.Patch(color='#F35D5DFF', label='ABX')
    PLA = mpatches.Patch(color='#5182CC', label='Placebo')
    axis3.legend(handles=[ABX, PLA], loc="lower right")
    
    #Name the axes
    axis3.set_xlabel("treatment", fontsize = 10)
    axis3.set_ylabel("log10(live bacteria/wet g)", fontsize = 10)
        
        
    vp=axis3.violinplot([x3,y3])
    #axis.scatter(x3, y3, marker="x")

    #Colors of the graphic
    colors=['#5182CC', '#F35D5DFF']
    edge_colors=['#0000FF', '#FF0000']
    
    for i, body in enumerate(vp['bodies']):
        body.set_facecolor(colors[i])
        body.set_edgecolor(edge_colors[i])
    
    figure3.legend(loc="right")
    figure3.savefig("Violin_ileal_figure.png", dpi=150)

#################################### Principal Script ###########################################

unique_mice = mice_id()
xvalue = 0
yvalue = 0  
xvalue2 = 0
yvalue2 = 0 
xvalue3 = 0
yvalue3 = 0 

### Empty the folders 'input' and 'images' ###
shutil.rmtree("input")
shutil.rmtree("images")
os.mkdir("input")
os.mkdir("images")


### Copy the CSV data file in a folder called 'input' ###
shutil.copy("data_small.csv", "input/data_small.csv")

### For each mouse, retrieve data and draw graphics ###
for mouse_id in unique_mice : 
    x=[]
    y=[]

    x2 = []
    y2 = []

    x3 = []
    y3 = []

    fd = open("data_small.csv", "r")
    #skip 1st line
    line = fd.readline()
    #retrieve 1st data line (2nd line )
    line = fd.readline()
    while line != '':
        #remove end of line character
        line = line.replace("\n", "")
        data = line.split(";")
        #filter by mouse ID
        if len(data) == 11:
            if data[4] == mouse_id : 
            #process only for fecal samples
                if data[2] == 'fecal' :
                    xvalue = float(data[7])
                    yvalue = math.log10(float(data[8]))
                    x.append(xvalue)
                    y.append(yvalue)
                    treatment = data[5]
            
            treat = data[5]
            #retrieve data for the violin graphic of cecal
            if data[2] == "cecal" :
                if treat == "ABX" :
                    xvalue2 = math.log10(float(data[8]))
                    x2.append(xvalue2)
                else :
                    yvalue2 = math.log10(float(data[8]))
                    y2.append(yvalue2)    
                
            #retrieve data for the violin graphic of ileal
            if data[2] == "ileal" :
                if treat == "ABX" :
                    xvalue3 = math.log10(float(data[8]))
                    x3.append(xvalue3)
                else :
                    yvalue3 = math.log10(float(data[8]))
                    y3.append(yvalue3)

        line = fd.readline()
    fd.close()
    
    #draw curve
    graphic_basic (x, y)
    violin_graphic_cecal (x2, y2,treat)
    violin_graphic_ileal (x3, y3,treat)

### Stock the graphics obtained in a folder called 'images' ###
shutil.copy("Basic_fecal_figure.png", "images/Basic_fecal_figure.png")
shutil.copy("Violin_cecal_figure.png", "images/Violin_cecal_figure.png")
shutil.copy("Violin_ileal_figure.png", "images/Violin_ileal_figure.png")


#################################### End of the principal script ###########################################


#Code python pour le projet d'informatique et biologie sur les souris 
