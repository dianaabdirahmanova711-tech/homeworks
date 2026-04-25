import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\Diana\Downloads\catalog_products (1).xlsx")


# форма
print("Форма:", df.shape)

# типы данных
print("\nТипы данных:")
print(df.dtypes)

# пропуски
print("\nПропуски:")
print(df.isnull().sum())

# первые 5 строк
print("\nПервые строки:")
print(df.head())


#2. Приведение типов и заполнение NaN
# числовые колонки (пример)
num_cols = df.columns[1:11]

# преобразование в float
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

# заполнение средним
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# проверка
print(df[num_cols].isnull().sum())
# 3. Новые колонки
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log(df['col_2'])
# 4. Фильтр дорогих Electronics
electronics_expensive = df[
    (df['col_2'] > 500) &
    (df['col_7'] == 'Electronics')
]

print(electronics_expensive.head())
#5. Группировка
grouped = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index()

print(grouped)
# 6. Статистика
stats = []

for col in num_cols:
    stats.append({
        'column': col,
        'mean': df[col].mean(),
        'median': df[col].median(),
        'std': df[col].std()
    })

stats_df = pd.DataFrame(stats)
print(stats_df)
# 7. Аномалии
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()

anomalies = df[df['col_2'] > mean_price + 3 * std_price]
print(anomalies.head())
#8. Корреляция
corr = df[num_cols].corr()
print(corr)
# 9. Гистограмма
plt.figure()
plt.hist(df['col_2'], bins=50)
plt.title("Распределение цены")
plt.xlabel("Цена")
plt.ylabel("Количество")
plt.grid()
plt.show()
# 10. Scatter + регрессия
sns.regplot(x='col_2', y='col_3', data=df)
plt.title("Цена vs Количество")
plt.show()
# 11. Boxplot
sns.boxplot(x='col_7', y='col_2', data=df)
plt.xticks(rotation=45)
plt.title("Цена по категориям")
plt.show()
# 12. Pairplot
sns.pairplot(df[['col_2','col_3','col_4','col_5','col_6','col_7']], hue='col_7')
plt.show()
# 13. Heatmap
sns.heatmap(corr, annot=True)
plt.title("Корреляция")
plt.show()
# 14. Сохранение
df.to_excel("catalog_analysis.xlsx", index=False)
#15. Итог по категориям
category_summary = df.groupby('col_7').agg(
    count=('col_1', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()

print(category_summary.head())
# 16. Самые дорогие
most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax()]
print(most_expensive[['col_1','col_2','col_7']])
# 17. Топ-10 по стоимости
top10 = df.sort_values(by='total_value', ascending=False).head(10)
print(top10[['col_1','col_2','col_3','total_value']])
#18. Диапазоны цен
bins = [0,50,200,500,1000,np.inf]
labels = ['0-50','50-200','200-500','500-1000','>1000']

df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)

price_counts = df['price_range'].value_counts().sort_index()

sns.barplot(x=price_counts.index, y=price_counts.values)
plt.show()
#19. Категория с max стоимостью
df['stock_value'] = df['col_2'] * df['col_3']

cat_value = df.groupby('col_7')['stock_value'].sum()

print(cat_value.sort_values(ascending=False))
# 22. Нет на складе
out_of_stock = df[df['col_3'] == 0]
print(out_of_stock[['col_1','col_7','col_2']].head(10))
# 23. Топ категории
top_categories = df['col_7'].value_counts().head(5)

sns.barplot(x=top_categories.values, y=top_categories.index)
plt.show()
# 24. Популярные товары
top_products = df.sort_values(by='col_3', ascending=False).head(10)

sns.barplot(x='col_3', y='col_1', data=top_products)
plt.show()
#25. Heatmap категории × цены
pivot = pd.pivot_table(
    df,
    values='col_1',
    index='col_7',
    columns='price_range',
    aggfunc='count'
)

sns.heatmap(pivot, annot=True)
plt.show()

#26. Средняя цена всех товаров
print(df['col_2'].mean())
# 27. Максимальный запас
print(df['col_3'].max())
#28. Минимальная цена
print(df['col_2'].min())
# 29. Товары дешевле 100
cheap = df[df['col_2'] < 100]
print(cheap.head())
#30. Сортировка по цене
sorted_df = df.sort_values(by='col_2')
# 31. Уникальные категории
print(df['col_7'].unique())
# 32. Количество категорий
print(df['col_7'].nunique())
# 33. Средний запас
print(df['col_3'].mean())
# 34. Самый дешёвый товар
print(df.loc[df['col_2'].idxmin()])
# 35. Самый дорогой товар
print(df.loc[df['col_2'].idxmax()])



# 36. Средняя цена и запас (scatter)
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
plt.xlabel("Средняя цена")
plt.ylabel("Средний запас")
plt.show()


# 37. Разброс цены (std)
std_price = df.groupby('col_7')['col_2'].std().reset_index()

sns.barplot(
    x='col_2',
    y='col_7',
    data=std_price
)

plt.title("Разброс цен по категориям")
plt.xlabel("Std цены")
plt.ylabel("Категория")
plt.show()


# 38. Товары без запаса
no_stock = df[df['col_3'] == 0]

print(no_stock[['col_1','col_7','col_2']].head(10))


# 39. Топ-5 категорий
top5 = df['col_7'].value_counts().head(5).reset_index()
top5.columns = ['category','count']

sns.barplot(x='count', y='category', data=top5)
plt.title("Топ-5 категорий")
plt.show()
# 40. Топ товары по запасу
top_stock = df.sort_values(by='col_3', ascending=False).head(10)

sns.barplot(x='col_3', y='col_1', data=top_stock)
plt.title("Топ товаров по количеству")
plt.show()
#41. Heatmap категории × цена
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
#42. Цена vs рейтинг
sns.regplot(x='col_2', y='col_5', data=df)

plt.title("Цена vs Рейтинг")
plt.xlabel("Цена")
plt.ylabel("Рейтинг")
plt.show()


# 43. Pairplot (связи)
sns.pairplot(
    df[['col_2','col_3','col_4','col_5','col_6','col_7']],
    hue='col_7'
)
plt.show()


# 44. Экстремальные товары
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()

mean_stock = df['col_3'].mean()
std_stock = df['col_3'].std()

extreme_items = df[
    (df['col_2'] > mean_price + 3*std_price) |
    (df['col_3'] > mean_stock + 3*std_stock)
]

print(extreme_items.head())


# 45. Финальный Excel отчет
with pd.ExcelWriter("catalog_final_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Main Data", index=False)
    category_summary.to_excel(writer, sheet_name="Category Summary", index=False)
    top10.to_excel(writer, sheet_name="Top Value", index=False)
    top_stock.to_excel(writer, sheet_name="Top Stock", index=False)