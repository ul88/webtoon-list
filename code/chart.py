import matplotlib.pyplot as plt
import pandas as pd


import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 생성
data = {
    "플랫폼": ["네이버 웹툰", "카카오페이지", "카카오웹툰", "레진코믹스", "인스타그램"],
    "응답 비율": [87.4, 35.0, 25.7, 15.6, 11.5]
}

# 중복 응답을 고려하여 데이터프레임 생성
df = pd.DataFrame(data)
df = df.sort_values(by="응답 비율", ascending=False)

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.bar(df["플랫폼"], df["응답 비율"], color='skyblue')
plt.title("사람들의 선호도")
plt.xlabel("플랫폼")
plt.ylabel("응답 비율 (%)")

# 그래프에 텍스트 표시 (옵션)
for i, v in enumerate(df["응답 비율"]):
    plt.text(i, v + 2, str(v) + '%', ha='center', va='bottom', fontsize=12)

plt.xticks(rotation=15)
plt.tight_layout()

# 그래프 표시
plt.show()
