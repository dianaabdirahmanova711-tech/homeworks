import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOAD
df = pd.read_excel(r"C:\Users\Diana\Downloads\catalog_products (1).xlsx")

# 2. CLEAN DATA
df.columns = df.columns.astype(str)

df = df.dropna()

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

df = df.dropna(subset=['col_2', 'col_3'])

df['col_7'] = df['col_7'].astype(str)

# 3. NEW FEATURES
df['log_price'] = np.log1p(df['col_2'])
df['total_value'] = df['col_2'] * df['col_3']
df['stock_value'] = df['col_2'] * df['col_3']

# 4. CORRELATION
corr = df[['col_2', 'col_3']].corr()

# 5. HISTOGRAM
plt.figure()
plt.hist(df['col_2'], bins=30)
plt.title("Распределение цены")
plt.xlabel("Цена")
plt.ylabel("Количество")
plt.grid()
plt.show()

# 6. REGRESSION
sns.regplot(x='col_2', y='col_3', data=df)
plt.title("Цена vs Количество")
plt.show()

# 7. BOXPLOT (fixed)
top_cats = df['col_7'].value_counts().head(10).index
df_box = df[df['col_7'].isin(top_cats)]

plt.figure(figsize=(10,5))
sns.boxplot(x='col_7', y='col_2', data=df_box)
plt.xticks(rotation=45)
plt.title("Цена по категориям")
plt.show()

# 8. PAIRPLOT
sns.pairplot(df[['col_2','col_3','col_4','col_5','col_6','col_7']], hue='col_7')
plt.show()

# 9. HEATMAP
sns.heatmap(corr, annot=True)
plt.title("Корреляция")
plt.show()

# 10. CATEGORY SUMMARY
category_summary = df.groupby('col_7').agg(
    count=('col_1', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()

print(category_summary.head())

# 11. MOST EXPENSIVE
most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax()]
print(most_expensive[['col_1','col_2','col_7']])

# 12. TOP 10 VALUE
top10 = df.sort_values(by='total_value', ascending=False).head(10)
print(top10[['col_1','col_2','col_3','total_value']])

# 13. PRICE BINS
bins = [0,50,200,500,1000,np.inf]
labels = ['0-50','50-200','200-500','500-1000','>1000']

df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)

price_counts = df['price_range'].value_counts().sort_index()

sns.barplot(x=price_counts.index, y=price_counts.values)
plt.title("Диапазоны цен")
plt.show()

# 14. CATEGORY STOCK VALUE
cat_value = df.groupby('col_7')['stock_value'].sum()
print(cat_value.sort_values(ascending=False))

# 15. OUT OF STOCK
out_of_stock = df[df['col_3'] == 0]
print(out_of_stock[['col_1','col_7','col_2']].head())

# 16. TOP CATEGORIES
top_categories = df['col_7'].value_counts().head(5)

sns.barplot(x=top_categories.values, y=top_categories.index)
plt.title("Топ категории")
plt.show()

# 17. TOP PRODUCTS BY STOCK
top_products = df.sort_values(by='col_3', ascending=False).head(10)

sns.barplot(x='col_3', y='col_1', data=top_products)
plt.title("Популярные товары")
plt.show()

# 18. PIVOT HEATMAP
pivot = pd.pivot_table(
    df,
    values='col_1',
    index='col_7',
    columns='price_range',
    aggfunc='count'
)

sns.heatmap(pivot, annot=True)
plt.title("Категории vs Цена")
plt.show()

# 19. BASIC STATS
print("Средняя цена:", df['col_2'].mean())
print("Макс запас:", df['col_3'].max())
print("Мин цена:", df['col_2'].min())

# 20. SAVE EXCEL
df.to_excel("catalog_analysis.xlsx", index=False)

with pd.ExcelWriter("catalog_final_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Main Data", index=False)
    category_summary.to_excel(writer, sheet_name="Category Summary", index=False)
    top10.to_excel(writer, sheet_name="Top Value", index=False)
    top_products.to_excel(writer, sheet_name="Top Stock", index=False)


# 21. Нет на складе
out_of_stock = df[df['col_3'] == 0]
print(out_of_stock[['col_1','col_7','col_2']].head(10))


# 22. Топ категории
top_categories = df['col_7'].value_counts().head(5)

sns.barplot(x=top_categories.values, y=top_categories.index)
plt.title("Топ категории")
plt.show()


# 23. Популярные товары
top_products = df.sort_values(by='col_3', ascending=False).head(10)

sns.barplot(x='col_3', y='col_1', data=top_products)
plt.title("Популярные товары")
plt.show()


# 24. Heatmap категории × цена
pivot = pd.pivot_table(
    df,
    values='col_1',
    index='col_7',
    columns='price_range',
    aggfunc='count'
)

sns.heatmap(pivot, annot=True)
plt.title("Категория vs Цена")
plt.show()


# 25. Средняя цена
print("Средняя цена:", df['col_2'].mean())


# 26. Максимальный запас
print("Макс запас:", df['col_3'].max())


# 27. Минимальная цена
print("Мин цена:", df['col_2'].min())


# 28. Дешевые товары
cheap = df[df['col_2'] < 100]
print(cheap.head())


# 29. Сортировка по цене
sorted_df = df.sort_values(by='col_2')


# 30. Уникальные категории
print(df['col_7'].unique())


# 31. Количество категорий
print(df['col_7'].nunique())


# 32. Средний запас
print(df['col_3'].mean())


# 33. Самый дешёвый товар
print(df.loc[df['col_2'].idxmin()])


# 34. Самый дорогой товар
print(df.loc[df['col_2'].idxmax()])


# 35. Средняя цена и запас
cat_stats = df.groupby('col_7').agg(
    mean_price=('col_2','mean'),
    mean_quantity=('col_3','mean')
).reset_index()

sns.scatterplot(
    x='mean_price',
    y='mean_quantity',
    hue='col_7',
    data=cat_stats
)

plt.title("Средняя цена vs Средний запас")
plt.show()


# 36. Разброс цен
std_price = df.groupby('col_7')['col_2'].std().reset_index()

sns.barplot(x='col_2', y='col_7', data=std_price)
plt.title("Разброс цен по категориям")
plt.show()


# 37. Нет в наличии
no_stock = df[df['col_3'] == 0]
print(no_stock[['col_1','col_7','col_2']].head(10))


# 38. Топ-5 категорий
top5 = df['col_7'].value_counts().head(5).reset_index()
top5.columns = ['category','count']

sns.barplot(x='count', y='category', data=top5)
plt.title("Топ-5 категорий")
plt.show()


# 39. Топ товары по запасу
top_stock = df.sort_values(by='col_3', ascending=False).head(10)

sns.barplot(x='col_3', y='col_1', data=top_stock)
plt.title("Топ товаров по количеству")
plt.show()


# 40. Heatmap категория × цена
pivot = pd.pivot_table(
    df,
    values='col_1',
    index='col_7',
    columns='price_range',
    aggfunc='count'
)

sns.heatmap(pivot, annot=True)
plt.title("Категория vs Цена")
plt.show()


# 41. Цена vs рейтинг
sns.regplot(x='col_2', y='col_5', data=df)
plt.title("Цена vs Рейтинг")
plt.show()


# 42. Pairplot
sns.pairplot(df[['col_2','col_3','col_4','col_5','col_6','col_7']], hue='col_7')
plt.show()


# 43. Экстремальные товары
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()

mean_stock = df['col_3'].mean()
std_stock = df['col_3'].std()

extreme_items = df[
    (df['col_2'] > mean_price + 3*std_price) |
    (df['col_3'] > mean_stock + 3*std_stock)
]

print(extreme_items.head())


# 44. Финальный Excel
with pd.ExcelWriter("catalog_final_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Main Data", index=False)
    category_summary.to_excel(writer, sheet_name="Category Summary", index=False)
    top10.to_excel(writer, sheet_name="Top Value", index=False)
    top_stock.to_excel(writer, sheet_name="Top Stock", index=False)