#import all python inbuilt libraries 
import pandas as pd #importing pandas
import matplotlib.pyplot as plt #importing pyplot from matplotlib
DE=pd.read_csv("latest_RAPTOR_player.csv") # reading the csv file
DE.head()# displaying the first 5 rows

DE.info() #getting the information about the entire data frame 

#The plot between pace impact and possession is plotted
x_ax=DE["pace_impact"]
y_ax_1=DE["poss"]
plt.plot(x_ax,y_ax_1)
plt.xlabel("PACE_IMPACT")
plt.ylabel("Posession Played")
plt.show

# The graph is clumsy with zigzag lines. We now plot multiple graphS. Three graphs are plotted:
#(i) pace impact vs possessions played
#(ii) pace_impact vs raptor_defense
#(iii) pace_impact vs raptor_offense
#For this, we define a new function as below.
def lin_plt3(x,y1,y2,y3): #plots three line plots x vs y1, x vs y2, x vs y3
  x_ax=DE[x]
  y_ax_1=DE[y1]
  y_ax_2=DE[y2]
  y_ax_3=DE[y3]
  fig,ax = plt.subplots()
  ax.plot(x_ax,y_ax_1)
  ax.plot(x_ax,y_ax_2)
  ax.plot(x_ax,y_ax_3)
  plt.xlabel("PACE_IMPACT")
  ax.legend((y1,y2,y3), loc='upper right', shadow=True)
  plt.show

lin_plt3(x="pace_impact",y1="poss",y2="raptor_defense",y3="raptor_offense") # calling the function to plot 3 line plots in a graph.

# We now plot three different scatter plots. For this, we define a new function as below.
def sct_plt3(x,y1,y2,y3): # plots three scatter plots x vs y1, x vs y2, x vs y3

  x_ax=DE[x]
  y_ax_1=DE[y1]
  y_ax_2=DE[y2]
  y_ax_3=DE[y3]
  
  plt.figure(0)
  plt.scatter(x_ax, y_ax_1, color="red")
  plt.xlabel(x)
  plt.ylabel(y1)
 
  plt.figure(1)
  plt.scatter(x_ax, y_ax_2, color="blue")
  plt.xlabel(x)
  plt.ylabel(y2)

  plt.figure(2)
  plt.scatter(x_ax, y_ax_3, color="green")
  plt.xlabel(x)
  plt.ylabel(y3)

sct_plt3(x="pace_impact",y1="poss",y2="raptor_defense",y3="raptor_offense") # calling the function to plot 3 scatter plots.

# we now plot histogram for each variable. For this, we define a new function as below.
def hist_plt3(y1,y2,y3,y4,nb): # plots histgrams for y1,y2,y3,y4 with the number of bins equal to nb
  y_ax_1=DE[y1]
  y_ax_2=DE[y2]
  y_ax_3=DE[y3]
  y_ax_3=DE[y4]
  
  plt.figure()
  plt.hist(DE[y1],bins = nb)
  plt.xlabel(y1)
   
 
  plt.figure()
  plt.hist(DE[y2],bins = nb)
  plt.xlabel(y2)
 

  plt.figure()
  plt.hist(DE[y3],bins = nb)
  plt.xlabel(y3)
 

  plt.figure()
  plt.hist(DE[y4],bins = nb)
  plt.xlabel(y4)

hist_plt3(y1="pace_impact",y2="poss",y3="raptor_defense",y4="raptor_offense",nb=100) # calling the function to plot 3 line plots in a graph.
