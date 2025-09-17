












import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Načtení dat
df = pd.read_csv('CA_Weather_Fire_Dataset_1984-2025.csv')
df['DATE'] = pd.to_datetime(df['DATE'])
df['FIRE_START_DAY'] = df['FIRE_START_DAY'].map({True: 1, False: 0})

# Summary statistiky
print(df.describe())

# Korelační heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Korelační matice')
plt.show()

# Časová řada požárů a teploty
df.set_index('DATE').resample('M')['FIRE_START_DAY', 'MAX_TEMP'].sum().plot()
plt.title('Měsíční počet požárů a průměrná teplota')
plt.show()

# Distribuce FIRE_COUNT
monthly_df = df.resample('M', on='DATE').agg({'FIRE_START_DAY': 'sum', 'MAX_TEMP': 'mean', 'PRECIPITATION': 'sum'})
monthly_df['FIRE_START_DAY'].hist(bins=20)
plt.title('Distribuce měsíčního počtu požárů')
plt.show()