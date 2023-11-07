import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = ['간편결제서비스(카카오페이,네이버페이 등)','신용카드 결제','휴대폰 소액결제','상품권(문화상품권, 해피머니 등)','계좌이체','기타']
y = [38.3,27.6,22.8,5.9,4.4,1.0]
bar = plt.bar(x,y, color = 'pink')
plt.ylim(0,40)

for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 12)

plt.title('웹툰 유료 결제 수단')
plt.show()