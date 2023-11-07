import matplotlib.pyplot as plt

# 연도별 데이터
years = [2020, 2021, 2022]
webtoon_usage = [21.2, 23.9, 24.7]

# 막대 차트 그리기
plt.bar(years, webtoon_usage, color='skyblue')

# 그래프 제목과 라벨 설정
plt.title('웹툰 매일 본 비율 (2020-2022)')
plt.xlabel('연도')
plt.ylabel('웹툰을 매일 본 비율')

# 각 막대 위에 해당 비율 표시
for i in range(len(years)):
    plt.text(years[i], webtoon_usage[i], f'{webtoon_usage[i]}%', ha='center', va='bottom')

# 그래프 표시
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
