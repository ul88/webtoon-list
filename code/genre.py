import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x=['코믹\n개그','액션','판타지','로맨스\n판타지','드라마']
y=[38.8,37.1,33.7,32.8,31.5]

plt.bar(x,y)
plt.title("즐겨보는 웹툰 장르 TOP5")
plt.show()