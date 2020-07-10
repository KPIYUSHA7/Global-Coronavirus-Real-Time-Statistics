#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the Libraries

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *


# In[3]:


#Fetch the data using Pandas

url = 'https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen'

df = pd.read_html(url, header=0)

df[0].drop(columns=['New cases (last 60 days)'], axis=1, inplace=True)

data = df[0]

Locations = list(data['Location'])

#Create the GUI using Tkinter

window = tk.Tk()
window.geometry("1600x1600")
window.configure(bg='SteelBlue4')

window.title("REAL-TIME CORONAVIRUS STATISTICS")

w = Label(window, text = "GLOBAL LIVE TRACKING METER FOR CORONAVIRUS CASES", bg = 'white', font = ('Comic sans MS', 15, 'bold'), fg = 'black')
w.grid(row=0,column=1)

frame = Frame(window) 
frame.grid(row=2,column=1) 
  
bottomframe = Frame(window) 
bottomframe.grid( row=6, column=1 ) 

displayframe = Frame(window)
displayframe.grid( row = 11, column= 1)

tkvar = StringVar(window)
choices = Locations
tkvar.set("United States")

popupMenu = OptionMenu(bottomframe, tkvar, *choices)
popupMenu.grid(row = 1,column=2)
popupMenu.configure(width=25, bg = "LightSalmon2")

figure = plt.Figure(figsize=(8,7), dpi=100)
ax1 = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, frame)
chart_type.get_tk_widget().grid(row=3, column = 1)
df1 = data[['Location','Cases per 1 million people']].groupby('Location').sum()
df1.plot(kind='barh', legend=True, ax=ax1, fontsize = 7, color = "red")
ax1.set_title('Cases Per Million People')

 
figure = plt.Figure(figsize=(8,7), dpi=100)
ax2 = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, frame)
chart_type.get_tk_widget().grid(row=3, column = 3)
df2 = data[['Location','Confirmed']].groupby('Location').sum()
df2.plot(kind='bar', legend=True, ax=ax2, fontsize = 6)
ax2.set_title('Confirmed Cases')

def showinfo(): 
    displayframe.grid(row=11,column=1)
    x = str(tkvar.get())
    confirmed = data.iloc[Locations.index(x), 1]
    cases_per_mil = data.iloc[Locations.index(x), 2]
    recovered = data.iloc[Locations.index(x), 3]
    deaths = data.iloc[Locations.index(x), 4] 
  
    a = tk.Label(displayframe, text = "Number of Confirmed Cases: {} \t".format(confirmed), font = ('Times', 12, 'bold'), fg = 'red').grid(row=11, column = 1)
    b = tk.Label(displayframe, text = "Number of Cases Per Million: {} \t".format(cases_per_mil), font = ('Times', 12, 'bold'), fg = 'red').grid(row=11, column = 2)
    c = tk.Label(displayframe, text = "Number of Recoveries: {} \t".format(recovered), font = ('Times', 12, 'bold'), fg = 'red').grid(row=11, column = 3)
    d = tk.Label(displayframe, text = "Number of Deaths: {} \t".format(deaths), font = ('Times', 12, 'bold'), fg = 'red').grid(row = 11, column= 4)
    
def clear():
    displayframe.grid_forget()   
        
B1 = Button(bottomframe, text="Update Statistics", command=showinfo)
B1.grid(row=1, column=5)
B1.configure(width = 18, bg = 'LightSteelBlue1')
B2 = Button(bottomframe, text="RESET", command=clear)
B2.configure(width = 18)
B2.grid(row=1, column =8)

window.mainloop()


# In[ ]:




