# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:14:42 2023

@author: dinse
"""
import pandas as pd
df = pd.read_csv("amazon.csv")
df.head()
df.describe()
df.info()
df.shape
df.dtypes
df.columns
"""
Index(['product_id', 'product_name', 'category', 'discounted_price',
       'actual_price', 'discount_percentage', 'rating', 'rating_count',
       'about_product', 'user_id', 'user_name', 'review_id', 'review_title',
       'review_content', 'img_link', 'product_link'],
      dtype='object')
"""
df.isnull().sum()
# Boş olan satırları bulma
boş_satırlar = df[df['rating_count'].isnull()]
boş_satırlar["rating_count"]#282 ve 324
df.rating_count
# rating_count sütununda virgülü kaldırma 
df['rating_count'] = df['rating_count'].str.replace(',','')
df['rating_count'] = df['rating_count'].astype("float64")
df.rating_count.mean()
df.rating_count.isnull().sum()
# 'rating count' sütunundaki boş değerlere ortalama değeri ata
mean_rating_count = df['rating_count'].mean()
df['rating_count'].fillna(mean_rating_count, inplace=True)
df.rating.sort_values(ascending = False)
# '|' değerli satırları sil
df = df[df['rating'] != '|']
# Rating değeri 5 ile 4.5 arasında olan satırları seçme
df['rating'] = df['rating'].astype("float64")
filtered_df = df[(df['rating'] >= 4.5) & (df['rating'] <= 5)]
pop_3 = filtered_df["rating"].sort_values(ascending = False ).head(3)
pop_3
#bazı sorgu ve filtrelemeler
df[df["rating"]==5.0][["category","product_name","actual_price"]]

import matplotlib.pyplot as plt
# Kategorilere göre gruplandırma yap
grouped_df = df.groupby('category').size()
grouped_df 
pop_10 = df.category.value_counts().head(10)#Computers&Accessories|Accessories&Peripherals|Cables&Accessories|Cables|USBCables                        233
pop_10
# Histogram grafiği oluştur
plt.figure(figsize=(6, 3))
pop_10.plot(kind='bar')
plt.xlabel('Kategori')
plt.ylabel('Ürün Sayısı')
plt.title('Kategorilere Göre Ürün Sayısı Histogramı')
plt.xticks(rotation=45, ha='right')  # Kategori etiketlerini 45 derece döndür ve sağa hizala
plt.tight_layout()
plt.show()

#sorgu2
df['actual_price'] = df['actual_price'].astype("float64")
df['actual_price'] = df['actual_price'].str.replace('₹','')
df['actual_price'] = df['actual_price'].str.replace(',','')
df[(df.category == "Computers&Accessories|Accessories&Peripherals|Cables&Accessories|Cables|USBCables")&(df.rating >= 4.0)]["actual_price"].mean()
df.actual_price

df.discount_percentage.sort_values(ascending = False)
df[df.discount_percentage >= str(80)]["discount_percentage"]
filtered_discount = df[(df['discount_percentage'] >= str(80)) & (df['discount_percentage'] <= str(99))]
filtered_discount









