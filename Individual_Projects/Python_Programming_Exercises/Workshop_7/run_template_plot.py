import matplotlib
import wx.grid

matplotlib.use('WXAgg') # allows Matplotlib to render plots within wxPython.
from matplotlib.pyplot import figure, ylable, plot, show
import numpy as np

def funct1():
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sizes = [10, 10, 10, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0) # explode the 1st slice (i.e. 'Apples')
 # Plot
 # autopct: A string that formats the percentage label for each slice. '%1.1f%%' means one decimal
 #place followed by a percent sign.
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True)
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
pass


#to embed a Matplotlib figure into a wxPanel in a wxPython application.

from template_frame_plot import GUIDemo as MyFrame

class MyMainFrame(MyFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.wx.Button
        self.Layout()
        self.Show(True)



if __name__ == "__main__":
    app = wx.App()
    frame = MyMainFrame()
    app.MainLoop()
    funct1()