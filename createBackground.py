import matplotlib.pyplot as plt  
import pandas as pd
import matplotlib.ticker as ticker
from numpy import arange

@ticker.FuncFormatter
def major_formatter(x, pos):
    return str(abs(x))

def drawVerticalLine(p, lineColor):
    width = 0.5
    plt.axvline(p, 0.3, 0.8, color=lineColor, linewidth=width)

def crearePanBackground():
    fig = plt.figure(figsize=(6, 2))
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().set_ticks([])
    plt.xlim(-1, 1)
    ax.xaxis.set_major_formatter(major_formatter)
    ax.tick_params(axis="x", direction="in", pad = -20, colors='white', labelsize=6)
    ax.xaxis.set_ticks([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75])
    ax.set_facecolor("xkcd:silver")
    fig.patch.set_facecolor("xkcd:silver")

    for p in arange(-0.75, 1.5, 0.25):
        drawVerticalLine(p, 'white')
    fig.savefig('pan_background.png', dpi=300)
    print("Saved!")

createMouseRect()
