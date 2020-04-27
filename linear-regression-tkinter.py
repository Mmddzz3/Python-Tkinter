from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import sys
import numpy as np
import matplotlib.pyplot as mpl
import locale
window = tk.Tk()
window.geometry("600x600")
window.title("GUI")
def calc_coef(x,y):
  n=len(x)
  meanX = np.mean(x)  
  meanY = np.mean(y)
  SSxy = np.sum(y*x) - n*meanX*meanY
  SSxx = np.sum(x*x) - n*meanX*meanX
  m = SSxy/SSxx
  c = meanY - m*meanX
  return (m,c)
def main():
    x=np.array([1,3,5,7,10,12,15,17,20,22,25,27,30,32,35,37,40,42,45,47,50]) 
    y=np.array([5.3,16.4,573.2,7.9,55.7,243.2,320.4,13.2,17.6,9.3,6.3,11.3,55.7,203.3,243.2,129.7,24.8,4.3,126.6,13.5,6.1]) 
    coef= calc_coef(x,y)     
    m=float(coef[0])
    c=float(coef[1])
    var = StringVar()  
    msg1 = Message( window, text = "X1 : 12  Then the respective predicted value is : 128.377718597424")    
    msg1.pack()
    plot_line(x,y,coef)
def plot_line(x,y,coef):
    mpl.scatter(x,y, color="green", s=30)
    y_cal= coef[0]*x + coef[1]
    mpl.plot(x,y_cal,color="yellow")
    mpl.xlabel('Item Weight')
    mpl.ylabel('Sales')
    mpl.show()   
menubar = Menu(window, bg="pink", fg="blue")  
menubar.add_command(label="Linear Regression" ,command =main)  
menubar.add_command(label="Quit", command=quit)
window.config(menu=menubar)  
var = StringVar()  
msg = Message( window, text ="LINEAR REGRESSION USING TKINTER", bg="pink",width=1080)    
msg.pack()
window.mainloop()
