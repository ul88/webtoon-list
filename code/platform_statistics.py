import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x1=['네이버\n웹툰','카카오\n페이지','카카오\n웹툰\n(다음 웹툰)','네이버\n시리즈','레진\n코믹스','인스타\n그램','탑툰','투믹스','페이스북','리디']
y1=[87.4,35.0,25.7,22.3,15.6,11.5,8.9,6.6,5.0,4.7]
plt.title("웹툰 주 이용 서비스(상위 10개)")
plt.bar(x1,y1)
plt.show()